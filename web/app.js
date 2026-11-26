/**
 * AGY Job Hunter & CV Commander — Complete Frontend Engine
 * Features:
 * 1. Multi-Profile Switching & Candidate Management
 * 2. Google Drive-Style File & Folder Explorer (Preview, Drag&Drop, Delete)
 * 3. Interactive ATS Job Board with Filtering & Search
 * 4. Human-in-the-Loop Transparent Application Workflow
 * 5. Instant CV Yaml Re-Render via RenderCV
 */

// Global Application State
const state = {
  activeProfileId: 'damar-fikrie',
  profiles: [],
  jobs: [],
  stats: {},
  projects: [],
  logs: [],
  activeJobId: null,
  activeJobDetail: null,
  filterCategory: 'all',
  filterStatus: 'pending_review',
  filterLocation: 'all',
  searchTerm: '',
  // Drive Explorer State
  explorerPath: '',
  explorerItems: [],
  explorerSelected: new Set(),
  activePreviewFile: null
};

// ==========================================================================
// UTILITY FUNCTIONS & API CLIENT
// ==========================================================================

function showToast(message, type = 'info') {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast-card toast-${type}`;
  toast.innerHTML = `
    <div class="toast-indicator"></div>
    <div class="toast-body">
      <div class="toast-msg">${escapeHtml(message)}</div>
    </div>
  `;

  container.appendChild(toast);
  setTimeout(() => {
    toast.classList.add('fade-out');
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

function parseMarkdown(md) {
  if (!md) return '<p class="placeholder-text">Tidak ada konten tersedia.</p>';
  
  let html = md.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');

  html = html.replace(/^### (.*$)/gim, '<h3>$1</h3>');
  html = html.replace(/^## (.*$)/gim, '<h2>$1</h2>');
  html = html.replace(/^# (.*$)/gim, '<h1>$1</h1>');
  html = html.replace(/^\> (.*$)/gim, '<blockquote>$1</blockquote>');

  // Tables
  const lines = html.split('\n');
  let inTable = false;
  let tableHtml = '';
  const newLines = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith('|') && line.endsWith('|')) {
      if (!inTable) {
        inTable = true;
        tableHtml = '<table><thead>';
        const headers = line.split('|').slice(1, -1).map(h => `<th>${h.trim()}</th>`).join('');
        tableHtml += `<tr>${headers}</tr></thead><tbody>`;
        if (i + 1 < lines.length && lines[i + 1].includes('---')) i++;
      } else {
        const cells = line.split('|').slice(1, -1).map(c => `<td>${c.trim()}</td>`).join('');
        tableHtml += `<tr>${cells}</tr>`;
      }
    } else {
      if (inTable) {
        tableHtml += '</tbody></table>';
        newLines.push(tableHtml);
        inTable = false;
      }
      newLines.push(line);
    }
  }
  if (inTable) {
    tableHtml += '</tbody></table>';
    newLines.push(tableHtml);
  }
  html = newLines.join('\n');

  html = html.replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>');
  html = html.replace(/\*(.*?)\*/gim, '<em>$1</em>');
  html = html.replace(/`([^`]+)`/gim, '<code>$1</code>');
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/gim, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  html = html.replace(/^- (.*$)/gim, '<li>$1</li>');
  html = html.replace(/^\d+\. (.*$)/gim, '<li>$1</li>');
  html = html.replace(/\n\n/gim, '<br><br>');

  return html;
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

async function apiGet(endpoint) {
  try {
    const res = await fetch(endpoint);
    if (!res.ok) {
      console.warn(`GET ${endpoint} returned status ${res.status}`);
      return null;
    }
    return await res.json();
  } catch (err) {
    console.error(`Error GET ${endpoint}:`, err);
    return null;
  }
}

async function apiPost(endpoint, data) {
  try {
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.error || `HTTP ${res.status}`);
    }
    return await res.json();
  } catch (err) {
    console.error(`Error POST ${endpoint}:`, err);
    showToast(err.message || `Gagal mengeksekusi aksi`, 'error');
    return null;
  }
}

// ==========================================================================
// APP INITIALIZATION
// ==========================================================================

document.addEventListener('DOMContentLoaded', async () => {
  setupNavigation();
  setupFilters();
  setupEditorialTabs();
  setupScraperDrawer();
  setupActionButtons();

  // Multi-Profile and Drive Explorer Setup
  setupProfileSwitcher();
  setupProfileModal();
  setupDriveExplorer();

  // Load all initial profile and board data
  await loadAllData();
});

async function loadAllData() {
  await Promise.all([
    loadProfiles(),
    loadStats(),
    loadJobs(),
    loadProjects(),
    loadLogs()
  ]);
}

// ==========================================================================
// 1. MULTI-PROFILE MANAGEMENT
// ==========================================================================

async function loadProfiles() {
  const res = await apiGet('/api/profiles');
  if (!res) return;

  state.profiles = res.profiles || [];
  state.activeProfileId = res.active_profile || 'damar-fikrie';

  const activeProf = state.profiles.find(p => p.id === state.activeProfileId) || state.profiles[0];
  if (activeProf) {
    // Update Header Chip
    const chipAvatar = document.getElementById('chip-avatar');
    const chipName = document.getElementById('chip-name');
    const chipRole = document.getElementById('chip-role');
    const dropTag = document.getElementById('dropdown-active-tag');

    if (chipAvatar) chipAvatar.textContent = activeProf.avatar || 'ID';
    if (chipName) chipName.textContent = activeProf.name;
    if (chipRole) chipRole.textContent = `${activeProf.title} • ${activeProf.industry_tag || activeProf.industry}`;
    if (dropTag) dropTag.textContent = activeProf.industry_tag || activeProf.industry;

    // Update Quick Scraper default keyword
    const scanKeyword = document.getElementById('scan-keyword');
    if (scanKeyword && activeProf.glints_keywords && activeProf.glints_keywords.length > 0) {
      scanKeyword.value = activeProf.glints_keywords[0];
    }

    // Update Right Sidebar Candidate Info
    const candName = document.getElementById('sidebar-candidate-name');
    const candEmail = document.getElementById('sidebar-candidate-email');
    const candLink = document.getElementById('sidebar-candidate-link');
    if (candName) candName.value = activeProf.name + (activeProf.education ? ` (${activeProf.education.split('—')[0].trim()})` : '');
    if (candEmail) candEmail.value = activeProf.email || '';
    if (candLink) candLink.value = activeProf.website || (activeProf.linkedin ? `https://linkedin.com/in/${activeProf.linkedin}` : '');

    // Update Page Title
    document.title = `AGY Job Hunter & CV Commander — ${activeProf.name}`;

    // Update Portfolio Tab Header
    const portHeading = document.getElementById('portfolio-heading');
    const portSubtext = document.getElementById('portfolio-subtext');
    const portBadges = document.getElementById('portfolio-badges');

    if (portHeading) portHeading.textContent = `Portofolio & Rekam Karya — ${activeProf.name}`;
    if (portSubtext) portSubtext.innerHTML = `Data proyek terverifikasi untuk <strong>${escapeHtml(activeProf.name)}</strong> (${escapeHtml(activeProf.title)}). Sumber kebenaran faktual untuk penyusunan CV tailored.`;

    if (portBadges) {
      if (activeProf.id === 'damar-fikrie') {
        portBadges.innerHTML = `
          <span class="source-badge"><span class="source-dot green"></span> Folder Lokal: 32 Items Terdata</span>
          <span class="source-badge"><span class="source-dot blue"></span> GitHub: KarmaSenzu</span>
          <span class="source-badge"><span class="source-dot purple"></span> Linux VPS: Deployed & Active</span>
        `;
      } else if (activeProf.id === 'galuh-lutfia') {
        portBadges.innerHTML = `
          <span class="source-badge"><span class="source-dot green"></span> CAD & Shop Drawing Terdata</span>
          <span class="source-badge"><span class="source-dot blue"></span> Tekla Structures & BIM</span>
          <span class="source-badge"><span class="source-dot purple"></span> BNSP Drafter Sipil Terverifikasi</span>
        `;
      } else {
        portBadges.innerHTML = `
          <span class="source-badge"><span class="source-dot green"></span> Berkas Terverifikasi</span>
          <span class="source-badge"><span class="source-dot blue"></span> ${escapeHtml(activeProf.industry_tag || activeProf.industry)}</span>
        `;
      }
    }
  }

  // Populate Dropdown List
  const container = document.getElementById('profile-list-container');
  if (!container) return;
  container.innerHTML = '';

  state.profiles.forEach(p => {
    const item = document.createElement('div');
    item.className = `profile-item ${p.id === state.activeProfileId ? 'active' : ''}`;
    
    const stats = p.stats || { total_jobs: 0, pending_jobs: 0, applied_jobs: 0 };
    item.innerHTML = `
      <div class="profile-item-avatar">${escapeHtml(p.avatar || 'ID')}</div>
      <div class="profile-item-info">
        <div class="profile-item-name">${escapeHtml(p.name)}</div>
        <div class="profile-item-sub">${escapeHtml(p.title)}</div>
      </div>
      <div class="profile-item-badge">${stats.total_jobs} Lowongan</div>
    `;

    item.addEventListener('click', async (e) => {
      e.stopPropagation();
      closeProfileDropdown();
      if (p.id !== state.activeProfileId) {
        await switchProfile(p.id);
      }
    });

    container.appendChild(item);
  });
}

function setupProfileSwitcher() {
  const chipBtn = document.getElementById('profile-chip-btn');
  const dropdown = document.getElementById('profile-dropdown-menu');
  const wrapper = document.getElementById('profile-switcher-wrapper');

  if (chipBtn && dropdown) {
    chipBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = dropdown.style.display === 'block';
      if (isOpen) {
        closeProfileDropdown();
      } else {
        dropdown.style.display = 'block';
        if (wrapper) wrapper.classList.add('open');
      }
    });

    document.addEventListener('click', (e) => {
      if (wrapper && !wrapper.contains(e.target)) {
        closeProfileDropdown();
      }
    });
  }
}

function closeProfileDropdown() {
  const dropdown = document.getElementById('profile-dropdown-menu');
  const wrapper = document.getElementById('profile-switcher-wrapper');
  if (dropdown) dropdown.style.display = 'none';
  if (wrapper) wrapper.classList.remove('open');
}

async function switchProfile(profileId) {
  showToast(`Beralih ke profil ${profileId}...`, 'info');
  const res = await apiPost('/api/profiles/active', { profile_id: profileId });
  if (res && res.success) {
    state.activeProfileId = profileId;
    state.activeJobId = null;
    state.filterStatus = 'all'; // Default to all so user immediately sees all jobs or empty state
    const statusSelect = document.getElementById('board-status-filter');
    if (statusSelect) statusSelect.value = 'all';
    document.querySelectorAll('.h-metric').forEach(m => {
      if (m.getAttribute('data-filter-status') === 'all') m.classList.add('active');
      else m.classList.remove('active');
    });

    showToast(res.message, 'success');
    await loadAllData();
    // Refresh explorer if open
    const expTab = document.querySelector('.nav-tab-btn[data-tab="tab-explorer"]');
    if (expTab && expTab.classList.contains('active')) {
      await loadExplorer('');
    }
  }
}

function setupProfileModal() {
  const modal = document.getElementById('modal-profile');
  const btnCreate = document.getElementById('btn-open-create-profile');
  const btnEdit = document.getElementById('btn-open-edit-profile');
  const btnClose = document.getElementById('btn-close-profile-modal');
  const btnCancel = document.getElementById('btn-cancel-profile');
  const btnDelete = document.getElementById('btn-delete-profile');
  const form = document.getElementById('profile-form');

  if (btnCreate) {
    btnCreate.addEventListener('click', () => {
      closeProfileDropdown();
      openProfileModal('create');
    });
  }

  if (btnEdit) {
    btnEdit.addEventListener('click', () => {
      closeProfileDropdown();
      openProfileModal('edit');
    });
  }

  if (btnClose) btnClose.addEventListener('click', closeProfileModal);
  if (btnCancel) btnCancel.addEventListener('click', closeProfileModal);
  if (btnDelete) btnDelete.addEventListener('click', deleteCurrentProfile);

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeProfileModal();
    });
  }

  // Setup CV Upload Dropzone inside Modal
  setupModalCvDropzone();

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const mode = document.getElementById('profile-form-mode').value;
      const id = document.getElementById('profile-form-id').value;

      const payload = {
        id: id,
        name: document.getElementById('prof-name').value.trim(),
        title: document.getElementById('prof-title').value.trim(),
        industry: document.getElementById('prof-industry').value.trim(),
        industry_tag: document.getElementById('prof-industry-tag').value.trim(),
        email: document.getElementById('prof-email').value.trim(),
        phone: document.getElementById('prof-phone').value.trim(),
        location: document.getElementById('prof-location').value.trim(),
        education: document.getElementById('prof-education').value.trim(),
        university: document.getElementById('prof-university').value.trim(),
        gpa: document.getElementById('prof-gpa').value.trim(),
        skills: document.getElementById('prof-skills').value.trim(),
        glints_keywords: document.getElementById('prof-keywords').value.trim(),
        cv_file_base64: window._pendingCvBase64 || null
      };

      const endpoint = mode === 'create' ? '/api/profiles/create' : '/api/profiles/update';
      showToast(`Menyimpan profil ${payload.name}...`, 'info');
      const res = await apiPost(endpoint, payload);
      if (res && res.success) {
        showToast(res.message, 'success');
        closeProfileModal();
        window._pendingCvBase64 = null;
        await loadAllData();
      }
    });
  }
}

function setupModalCvDropzone() {
  const dropzone = document.getElementById('profile-cv-dropzone');
  const fileInput = document.getElementById('profile-cv-input');
  const filenameLabel = document.getElementById('cv-drop-filename');

  if (!dropzone || !fileInput) return;

  dropzone.addEventListener('click', () => fileInput.click());

  dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.classList.add('dragover');
  });

  ['dragleave', 'dragend'].forEach(evt => {
    dropzone.addEventListener(evt, () => dropzone.classList.remove('dragover'));
  });

  dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.classList.remove('dragover');
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      handleModalCvFile(e.dataTransfer.files[0]);
    }
  });

  fileInput.addEventListener('change', () => {
    if (fileInput.files && fileInput.files.length > 0) {
      handleModalCvFile(fileInput.files[0]);
    }
  });

  function handleModalCvFile(file) {
    if (filenameLabel) {
      filenameLabel.innerHTML = `📄 <strong>${escapeHtml(file.name)}</strong> (${(file.size / 1024).toFixed(1)} KB)`;
    }
    const reader = new FileReader();
    reader.onload = (e) => {
      window._pendingCvBase64 = e.target.result;
      showToast(`CV ${file.name} siap diunggah saat formulir disimpan`, 'info');
    };
    reader.readAsDataURL(file);
  }
}

function openProfileModal(mode = 'create') {
  const modal = document.getElementById('modal-profile');
  const title = document.getElementById('profile-modal-title');
  const modeInput = document.getElementById('profile-form-mode');
  const idInput = document.getElementById('profile-form-id');
  const btnDelete = document.getElementById('btn-delete-profile');
  const filenameLabel = document.getElementById('cv-drop-filename');

  window._pendingCvBase64 = null;
  if (filenameLabel) {
    filenameLabel.innerHTML = `Tarik & Lepaskan berkas CV ke sini, atau <span class="text-cyan clickable">klik untuk memilih</span>`;
  }

  if (mode === 'create') {
    title.innerHTML = `<span>👤</span> Tambah Profil Kandidat Baru`;
    modeInput.value = 'create';
    idInput.value = '';
    btnDelete.style.display = 'none';
    document.getElementById('profile-form').reset();
  } else {
    const current = state.profiles.find(p => p.id === state.activeProfileId);
    if (!current) return;

    title.innerHTML = `<span>✏️</span> Edit Data Profil — ${escapeHtml(current.name)}`;
    modeInput.value = 'edit';
    idInput.value = current.id;
    btnDelete.style.display = state.profiles.length > 1 ? 'inline-block' : 'none';

    document.getElementById('prof-name').value = current.name || '';
    document.getElementById('prof-title').value = current.title || '';
    document.getElementById('prof-industry').value = current.industry || '';
    document.getElementById('prof-industry-tag').value = current.industry_tag || '';
    document.getElementById('prof-email').value = current.email || '';
    document.getElementById('prof-phone').value = current.phone || '';
    document.getElementById('prof-location').value = current.location || '';
    document.getElementById('prof-education').value = current.education || '';
    document.getElementById('prof-university').value = current.university || '';
    document.getElementById('prof-gpa').value = current.gpa || '';
    document.getElementById('prof-skills').value = Array.isArray(current.skills) ? current.skills.join(', ') : (current.skills || '');
    document.getElementById('prof-keywords').value = Array.isArray(current.glints_keywords) ? current.glints_keywords.join(', ') : (current.glints_keywords || '');
  }

  modal.style.display = 'flex';
}

function closeProfileModal() {
  const modal = document.getElementById('modal-profile');
  if (modal) modal.style.display = 'none';
}

async function deleteCurrentProfile() {
  const current = state.profiles.find(p => p.id === state.activeProfileId);
  if (!current) return;

  if (confirm(`Apakah Anda yakin ingin menghapus profil "${current.name}" beserta seluruh berkas CV dan lamarannya? Tindakan ini tidak dapat dibatalkan.`)) {
    showToast(`Menghapus profil ${current.name}...`, 'info');
    const res = await apiPost('/api/profiles/delete', { profile_id: current.id });
    if (res && res.success) {
      showToast(res.message, 'success');
      closeProfileModal();
      await loadAllData();
    }
  }
}

// ==========================================================================
// 2. GOOGLE DRIVE-STYLE FOLDER & FILE EXPLORER
// ==========================================================================

async function loadExplorer(path = '') {
  state.explorerPath = path;
  state.explorerSelected.clear();
  updateBulkDeleteBtn();

  const tbody = document.getElementById('explorer-tbody');
  if (tbody) {
    tbody.innerHTML = `
      <tr>
        <td colspan="5" style="text-align: center; padding: 30px; color: var(--text-dim);">
          <div class="spinner" style="margin: 0 auto 10px;"></div>
          Memuat berkas direktori...
        </td>
      </tr>
    `;
  }

  const res = await apiGet(`/api/explorer?path=${encodeURIComponent(path)}`);
  if (!res) return;

  state.explorerItems = res.items || [];
  renderExplorerBreadcrumbs(res.breadcrumbs || []);
  renderExplorerItems(res.items || []);
}

function renderExplorerBreadcrumbs(breadcrumbs) {
  const container = document.getElementById('explorer-breadcrumbs');
  if (!container) return;
  container.innerHTML = '';

  breadcrumbs.forEach((crumb, idx) => {
    const isLast = idx === breadcrumbs.length - 1;
    const crumbSpan = document.createElement('span');
    crumbSpan.className = `crumb ${isLast ? 'active' : 'clickable'}`;
    crumbSpan.textContent = idx === 0 ? `📁 ${crumb.name}` : crumb.name;
    crumbSpan.setAttribute('data-path', crumb.path);

    if (!isLast) {
      crumbSpan.addEventListener('click', () => loadExplorer(crumb.path));
    }

    container.appendChild(crumbSpan);
    if (!isLast) {
      const sep = document.createElement('span');
      sep.className = 'crumb-sep';
      sep.textContent = '/';
      container.appendChild(sep);
    }
  });
}

function renderExplorerItems(items) {
  const tbody = document.getElementById('explorer-tbody');
  if (!tbody) return;
  tbody.innerHTML = '';

  if (items.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="5" style="text-align: center; padding: 40px; color: var(--text-dim);">
          <p>Folder ini kosong.</p>
        </td>
      </tr>
    `;
    return;
  }

  items.forEach(item => {
    const tr = document.createElement('tr');
    tr.className = 'explorer-row';
    tr.setAttribute('data-path', item.path);

    let icon = '📄';
    if (item.is_dir) icon = '📁';
    else if (item.ext === 'pdf') icon = '📕';
    else if (['yaml', 'yml'].includes(item.ext)) icon = '⚙️';
    else if (['md', 'txt'].includes(item.ext)) icon = '📝';
    else if (['jpg', 'jpeg', 'png', 'svg', 'webp'].includes(item.ext)) icon = '🖼️';
    else if (item.ext === 'csv') icon = '📊';

    tr.innerHTML = `
      <td>
        <div class="explorer-item-name clickable">
          <input type="checkbox" class="explorer-checkbox" data-path="${escapeHtml(item.path)}">
          <span class="item-icon">${icon}</span>
          <span>${escapeHtml(item.name)}</span>
        </div>
      </td>
      <td><span class="tag-badge ${item.is_dir ? 'violet' : ''}">${escapeHtml(item.is_dir ? 'Folder' : item.ext ? '.' + item.ext : 'File')}</span></td>
      <td style="font-family: var(--font-mono); font-size: 11.5px; color: var(--text-dim);">${escapeHtml(item.size)}</td>
      <td style="font-family: var(--font-mono); font-size: 11.5px; color: var(--text-dim);">${escapeHtml(item.modified)}</td>
      <td>
        <div class="explorer-row-actions">
          ${item.is_dir ? `
            <button class="btn btn-secondary btn-sm btn-open-folder" data-path="${escapeHtml(item.path)}">Buka</button>
          ` : `
            <button class="btn btn-secondary btn-sm btn-preview-file" data-path="${escapeHtml(item.path)}" data-ext="${item.ext}" data-name="${escapeHtml(item.name)}">Lihat</button>
            <a href="/api/explorer/file?path=${encodeURIComponent(item.path)}" class="btn btn-secondary btn-sm" download title="Unduh">⬇️</a>
          `}
          ${item.is_deletable ? `
            <button class="btn-delete-job" data-del-path="${escapeHtml(item.path)}" title="Hapus berkas / folder">🗑️</button>
          ` : ''}
        </div>
      </td>
    `;

    // Row selection checkbox
    const chk = tr.querySelector('.explorer-checkbox');
    chk.addEventListener('click', (e) => {
      e.stopPropagation();
      if (chk.checked) state.explorerSelected.add(item.path);
      else state.explorerSelected.delete(item.path);
      updateBulkDeleteBtn();
    });

    // Double click / item name click
    const nameEl = tr.querySelector('.explorer-item-name');
    nameEl.addEventListener('click', () => {
      if (item.is_dir) {
        loadExplorer(item.path);
      } else {
        previewExplorerFile(item.path, item.ext, item.name);
      }
    });

    // Open Folder Button
    const btnOpen = tr.querySelector('.btn-open-folder');
    if (btnOpen) {
      btnOpen.addEventListener('click', () => loadExplorer(item.path));
    }

    // Preview File Button
    const btnPrev = tr.querySelector('.btn-preview-file');
    if (btnPrev) {
      btnPrev.addEventListener('click', () => previewExplorerFile(item.path, item.ext, item.name));
    }

    // Delete Single Item Button
    const btnDel = tr.querySelector('[data-del-path]');
    if (btnDel) {
      btnDel.addEventListener('click', async (e) => {
        e.stopPropagation();
        if (confirm(`Apakah Anda yakin ingin menghapus "${item.name}"?`)) {
          await deleteExplorerPaths([item.path]);
        }
      });
    }

    tbody.appendChild(tr);
  });
}

function updateBulkDeleteBtn() {
  const btn = document.getElementById('btn-explorer-bulk-delete');
  const countEl = document.getElementById('delete-count');
  const chkAll = document.getElementById('check-all-explorer');

  const count = state.explorerSelected.size;
  if (countEl) countEl.textContent = count;
  if (btn) btn.style.display = count > 0 ? 'inline-flex' : 'none';

  if (chkAll) {
    chkAll.checked = count > 0 && count === state.explorerItems.length;
  }
}

async function deleteExplorerPaths(paths) {
  showToast(`Menghapus ${paths.length} item...`, 'info');
  const res = await apiPost('/api/explorer/delete', { paths });
  if (res && res.success) {
    showToast(res.message, 'success');
    await loadExplorer(state.explorerPath);
    await loadStats();
    await loadJobs();
  }
}

function setupDriveExplorer() {
  const btnUp = document.getElementById('btn-explorer-up');
  const btnRefresh = document.getElementById('btn-explorer-refresh');
  const btnBulkDelete = document.getElementById('btn-explorer-bulk-delete');
  const chkAll = document.getElementById('check-all-explorer');
  const btnUpload = document.getElementById('btn-trigger-upload');
  const fileInput = document.getElementById('explorer-file-input');
  const dropzone = document.getElementById('explorer-dropzone');
  const btnClosePreview = document.getElementById('btn-close-preview');

  if (btnUp) {
    btnUp.addEventListener('click', () => {
      if (!state.explorerPath) return;
      const parts = state.explorerPath.split('/');
      parts.pop();
      loadExplorer(parts.join('/'));
    });
  }

  if (btnRefresh) {
    btnRefresh.addEventListener('click', () => loadExplorer(state.explorerPath));
  }

  if (chkAll) {
    chkAll.addEventListener('change', () => {
      const isChecked = chkAll.checked;
      document.querySelectorAll('.explorer-checkbox').forEach(cb => {
        cb.checked = isChecked;
        const p = cb.getAttribute('data-path');
        if (isChecked) state.explorerSelected.add(p);
        else state.explorerSelected.delete(p);
      });
      updateBulkDeleteBtn();
    });
  }

  if (btnBulkDelete) {
    btnBulkDelete.addEventListener('click', async () => {
      const paths = Array.from(state.explorerSelected);
      if (paths.length === 0) return;
      if (confirm(`Hapus ${paths.length} item terpilih secara permanen?`)) {
        await deleteExplorerPaths(paths);
      }
    });
  }

  if (btnUpload && fileInput) {
    btnUpload.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', () => {
      if (fileInput.files && fileInput.files.length > 0) {
        uploadFilesToExplorer(fileInput.files);
      }
    });
  }

  // Setup Drag & Drop Upload into Explorer Table
  if (dropzone) {
    ['dragenter', 'dragover'].forEach(evt => {
      dropzone.addEventListener(evt, (e) => {
        e.preventDefault();
        dropzone.classList.add('dragover');
      });
    });

    ['dragleave', 'dragend', 'drop'].forEach(evt => {
      dropzone.addEventListener(evt, () => dropzone.classList.remove('dragover'));
    });

    dropzone.addEventListener('drop', (e) => {
      e.preventDefault();
      if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
        uploadFilesToExplorer(e.dataTransfer.files);
      }
    });
  }

  if (btnClosePreview) {
    btnClosePreview.addEventListener('click', closeExplorerPreview);
  }
}

async function uploadFilesToExplorer(files) {
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    showToast(`Mengunggah "${file.name}" ke ${state.explorerPath || 'Root'}...`, 'info');

    const reader = new FileReader();
    reader.onload = async (e) => {
      const base64 = e.target.result;
      const res = await apiPost('/api/explorer/upload', {
        target_dir: state.explorerPath,
        filename: file.name,
        file_base64: base64
      });
      if (res && res.success) {
        showToast(res.message, 'success');
        await loadExplorer(state.explorerPath);
      }
    };
    reader.readAsDataURL(file);
  }
}

async function previewExplorerFile(path, ext, name) {
  const drawer = document.getElementById('explorer-preview-drawer');
  const filenameEl = document.getElementById('preview-filename');
  const filepathEl = document.getElementById('preview-filepath');
  const downloadBtn = document.getElementById('btn-preview-download');
  const contentArea = document.getElementById('preview-content-area');

  if (!drawer || !contentArea) return;

  state.activePreviewFile = { path, ext, name };
  if (filenameEl) filenameEl.textContent = name;
  if (filepathEl) filepathEl.textContent = path;
  if (downloadBtn) downloadBtn.href = `/api/explorer/file?path=${encodeURIComponent(path)}`;

  contentArea.innerHTML = '<div class="spinner" style="margin:40px auto;"></div>';
  drawer.classList.add('open');

  if (ext === 'pdf') {
    contentArea.innerHTML = `
      <iframe src="/api/explorer/file?path=${encodeURIComponent(path)}#toolbar=1" style="width:100%; height:100%; border:none; border-radius:8px;"></iframe>
    `;
  } else if (['jpg', 'jpeg', 'png', 'svg', 'webp'].includes(ext)) {
    contentArea.innerHTML = `
      <div style="display:flex; justify-content:center; align-items:center; height:100%; background:var(--bg-base); padding:20px;">
        <img src="/api/explorer/file?path=${encodeURIComponent(path)}" style="max-width:100%; max-height:100%; border-radius:8px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
      </div>
    `;
  } else if (['md', 'markdown', 'txt', 'log', 'yaml', 'yml', 'json', 'csv'].includes(ext)) {
    try {
      const res = await fetch(`/api/explorer/file?path=${encodeURIComponent(path)}`);
      const text = await res.text();
      if (['md', 'markdown'].includes(ext)) {
        contentArea.innerHTML = `<div class="markdown-body" style="padding: 20px;">${parseMarkdown(text)}</div>`;
      } else {
        contentArea.innerHTML = `<pre class="code-preview" style="padding: 18px; margin: 0; font-family: var(--font-mono); font-size: 12px; line-height: 1.6; color: var(--text-body); background: var(--bg-surface); overflow: auto; height: 100%;">${escapeHtml(text)}</pre>`;
      }
    } catch (err) {
      contentArea.innerHTML = `<p style="padding: 20px; color: var(--accent-rose);">Gagal memuat pratinjau teks: ${escapeHtml(err.message)}</p>`;
    }
  } else {
    contentArea.innerHTML = `
      <div style="text-align: center; padding: 60px 20px; color: var(--text-dim);">
        <p>Pratinjau berkas <strong>.${escapeHtml(ext)}</strong> tidak didukung secara langsung.</p>
        <a href="/api/explorer/file?path=${encodeURIComponent(path)}" class="btn btn-primary" download style="margin-top: 14px;">Unduh Berkas Ini</a>
      </div>
    `;
  }
}

function closeExplorerPreview() {
  const drawer = document.getElementById('explorer-preview-drawer');
  if (drawer) drawer.classList.remove('open');
  state.activePreviewFile = null;
}

// ==========================================================================
// 3. STATS & INTERACTIVE JOB BOARD
// ==========================================================================

async function loadStats() {
  const stats = await apiGet('/api/stats');
  if (!stats) return;
  state.stats = stats;

  const setEl = (id, val) => {
    const el = document.getElementById(id);
    if (el) el.textContent = val;
  };

  setEl('stat-total', stats.total_scanned || stats.total_tracked || 0);
  setEl('stat-pending', stats.pending_review || 0);
  setEl('stat-ready', stats.ready_to_submit || 0);
  setEl('stat-applied', stats.applied || 0);
  setEl('stat-pipeline', stats.in_pipeline || 0);
  setEl('stat-skipped', stats.skipped || 0);
  setEl('stat-projects', `${(stats.profile && stats.profile.verified_projects) || 10}+ Proyek`);
  setEl('badge-pending-count', stats.pending_review || 0);
}

async function loadJobs() {
  const jobs = await apiGet('/api/jobs');
  if (!jobs) return;
  state.jobs = jobs;

  renderMasterJobList();

  // Auto-select first matching job or active
  if (state.jobs.length > 0) {
    const currentStillExists = state.jobs.find(j => j.job_id === state.activeJobId);
    if (currentStillExists) {
      await selectJob(state.activeJobId);
    } else {
      const firstJob = state.jobs.find(j => j.status === state.filterStatus) || state.jobs[0];
      await selectJob(firstJob.job_id);
    }
  } else {
    state.activeJobId = null;
    clearJobDetailPanel();
  }
}

function clearJobDetailPanel() {
  const emptyState = document.getElementById('detail-empty-state');
  const activeWrapper = document.getElementById('detail-active-wrapper');
  if (emptyState) emptyState.style.display = 'flex';
  if (activeWrapper) activeWrapper.style.display = 'none';

  const title = document.getElementById('detail-role-title');
  const comp = document.getElementById('detail-company-name');
  if (title) title.textContent = 'Tidak Ada Lowongan';
  if (comp) comp.textContent = 'Pilih lowongan dari daftar atau jalankan scraper.';

  const pdfFrame = document.getElementById('detail-pdf-frame');
  if (pdfFrame) pdfFrame.src = '';

  const pitch = document.getElementById('apply-card-pitch');
  if (pitch) pitch.value = '';

  const yamlEditor = document.getElementById('detail-yaml-editor');
  if (yamlEditor) yamlEditor.value = '';

  const etabReadme = document.getElementById('etab-readme');
  if (etabReadme) etabReadme.innerHTML = '<p class="placeholder-text">Tidak ada data lowongan aktif untuk profil ini.</p>';
}

function renderMasterJobList() {
  const container = document.getElementById('job-compact-list');
  if (!container) return;
  container.innerHTML = '';

  const filtered = state.jobs.filter(j => {
    if (state.filterCategory !== 'all' && j.category !== state.filterCategory) return false;
    if (state.filterStatus !== 'all') {
      if (state.filterStatus === 'in_pipeline') {
        if (!['screening', 'test_assigned', 'interview_hr', 'interview_tech', 'offered'].includes(j.status)) return false;
      } else if (j.status !== state.filterStatus) {
        return false;
      }
    }
    if (state.filterLocation === 'Jakarta' && !j.location.toLowerCase().includes('jakarta')) return false;
    if (state.filterLocation === 'Remote' && !j.location.toLowerCase().includes('remote') && !j.work_mode.toLowerCase().includes('remote')) return false;
    if (state.searchTerm) {
      const term = state.searchTerm.toLowerCase();
      const matchRole = (j.role || '').toLowerCase().includes(term);
      const matchComp = (j.company || '').toLowerCase().includes(term);
      const matchCat = (j.category || '').toLowerCase().includes(term);
      if (!matchRole && !matchComp && !matchCat) return false;
    }
    return true;
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="loading-state">
        <p>Tidak ada lowongan dengan filter ini.</p>
      </div>
    `;
    return;
  }

  filtered.forEach(job => {
    const item = document.createElement('div');
    item.className = `job-item-card ${job.job_id === state.activeJobId ? 'active' : ''}`;
    item.setAttribute('data-id', job.job_id);

    let statusBadgeHtml = '';
    if (job.status === 'ready_to_submit') {
      statusBadgeHtml = `<span class="job-status-pill ready">🌐 Siap Submit</span>`;
    } else if (job.status === 'applied') {
      statusBadgeHtml = `<span class="job-status-pill applied">📤 Applied</span>`;
    } else if (job.status === 'screening') {
      statusBadgeHtml = `<span class="job-status-pill screening">👀 Screening</span>`;
    } else if (job.status === 'test_assigned') {
      statusBadgeHtml = `<span class="job-status-pill in_pipeline">💻 Tes Koding</span>`;
    } else if (job.status === 'interview_hr' || job.status === 'interview_tech') {
      statusBadgeHtml = `<span class="job-status-pill interview">🎙️ Interview</span>`;
    } else if (job.status === 'offered') {
      statusBadgeHtml = `<span class="job-status-pill offered">🎉 Offered</span>`;
    } else if (job.status === 'rejected') {
      statusBadgeHtml = `<span class="job-status-pill rejected">❌ Ditolak</span>`;
    } else if (job.status === 'skipped') {
      statusBadgeHtml = `<span class="job-status-pill skipped">Dilewati</span>`;
    } else {
      statusBadgeHtml = `<span class="job-status-pill pending">⏳ Antrean</span>`;
    }

    item.innerHTML = `
      <div class="job-item-top">
        <span class="job-item-company">${escapeHtml(job.company)}</span>
        <div style="display: flex; align-items: center; gap: 6px;">
          ${statusBadgeHtml}
          <button class="btn-delete-job" data-del-job="${escapeHtml(job.job_id)}" title="Hapus lowongan & folder">🗑️</button>
        </div>
      </div>
      <h4 class="job-item-title">${escapeHtml(job.role)}</h4>
      <div class="job-item-bottom">
        <span class="job-item-salary">${escapeHtml(job.salary)}</span>
        <span class="job-item-tag">${(job.work_mode || '').includes('Remote') ? 'Remote' : 'Hybrid / Onsite'}</span>
      </div>
    `;

    // Click select job
    item.addEventListener('click', () => {
      document.querySelectorAll('.job-item-card').forEach(c => c.classList.remove('active'));
      item.classList.add('active');
      selectJob(job.job_id);
    });

    // Delete job click
    const btnDel = item.querySelector('[data-del-job]');
    if (btnDel) {
      btnDel.addEventListener('click', async (e) => {
        e.stopPropagation();
        if (confirm(`Apakah Anda yakin ingin menghapus lowongan "${job.company} - ${job.role}" beserta foldernya?`)) {
          showToast(`Menghapus lowongan ${job.job_id}...`, 'info');
          const res = await apiPost('/api/jobs/delete', { job_id: job.job_id });
          if (res && res.success) {
            showToast(res.message, 'success');
            await loadJobs();
            await loadStats();
          }
        }
      });
    }

    container.appendChild(item);
  });
}

// ==========================================================================
// 4. SELECT JOB & POPULATE EDITORIAL DETAIL (RIGHT PANEL)
// ==========================================================================

async function selectJob(jobId) {
  state.activeJobId = jobId;

  document.querySelectorAll('.job-item-card').forEach(c => {
    if (c.getAttribute('data-id') === jobId) c.classList.add('active');
    else c.classList.remove('active');
  });

  const detail = await apiGet(`/api/job/${jobId}`);
  if (!detail) return;
  state.activeJobDetail = detail;

  const job = state.jobs.find(j => j.job_id === jobId) || {};

  // Show active wrapper, hide empty state
  const emptyState = document.getElementById('detail-empty-state');
  const activeWrapper = document.getElementById('detail-active-wrapper');
  if (emptyState) emptyState.style.display = 'none';
  if (activeWrapper) activeWrapper.style.display = 'block';

  // Header Details
  const roleTitle = document.getElementById('detail-role-title');
  const compName = document.getElementById('detail-company-name');
  const compBrief = document.getElementById('detail-company-brief');
  const catCrumb = document.getElementById('detail-category-crumb');
  const matchPill = document.getElementById('detail-match-pill');

  if (roleTitle) roleTitle.textContent = job.role || (detail.meta && detail.meta.role) || 'Software Engineer';
  if (compName) compName.textContent = job.company || (detail.meta && detail.meta.company) || 'Perusahaan';
  if (compBrief) compBrief.textContent = (detail.meta && detail.meta.industry) || job.category || 'Lowongan Kerja';
  if (catCrumb) catCrumb.textContent = `Careers / ${job.category || 'General'}`;
  if (matchPill) matchPill.textContent = `⚡ ${job.match_score || '100%'} Match (Rule 1 Verified)`;

  // 4 Specs Boxes
  const specLoc = document.getElementById('detail-spec-location');
  const specType = document.getElementById('detail-spec-type');
  const specSalary = document.getElementById('detail-spec-salary');
  const specDeadline = document.getElementById('detail-spec-deadline');

  if (specLoc) specLoc.textContent = job.location || (detail.meta && detail.meta.location) || 'Indonesia';
  if (specType) specType.textContent = job.work_mode || (detail.meta && detail.meta.work_mode) || 'Hybrid / Onsite';
  if (specSalary) specSalary.textContent = job.salary || (detail.meta && detail.meta.salary) || 'Kompetitif';
  if (specDeadline) specDeadline.textContent = job.deadline || (detail.meta && detail.meta.deadline) || 'Terbuka / Aktif';

  // External Portal Link
  const portalLink = document.getElementById('detail-job-external-link');
  const jobUrl = (detail.meta && (detail.meta.job_url || detail.meta.apply_url)) || job.job_url;
  if (portalLink) {
    if (jobUrl) {
      portalLink.href = jobUrl;
      portalLink.style.display = 'inline-flex';
    } else {
      portalLink.style.display = 'none';
    }
  }

  // File Path Display in Sidebar
  const folderDisplay = document.getElementById('apply-card-folder-display');
  if (folderDisplay) {
    const fullPath = detail.absolute_folder || (detail.folder ? `output/${detail.folder}` : 'Folder telah diarsipkan');
    folderDisplay.textContent = fullPath;
    folderDisplay.setAttribute('data-full-path', fullPath);
  }

  // CV PDF Elements (Tabs & Sidebar)
  const pdfFrame = document.getElementById('detail-pdf-frame');
  const etabPdfName = document.getElementById('etab-pdf-filename');
  const etabPdfOpen = document.getElementById('etab-pdf-open-tab');
  const cardPdfName = document.getElementById('apply-card-pdf-name');
  const cardPdfView = document.getElementById('apply-card-pdf-view');
  const cardPdfDownload = document.getElementById('apply-card-pdf-download');

  const pdfUrl = detail.pdf_url || '';
  const pdfName = detail.pdf_filename || 'CV_Kandidat.pdf';

  if (pdfFrame) {
    pdfFrame.src = pdfUrl ? `${pdfUrl}#toolbar=1` : '';
  }
  if (etabPdfName) etabPdfName.textContent = pdfName;
  if (etabPdfOpen) etabPdfOpen.href = pdfUrl || '#';
  if (cardPdfName) cardPdfName.textContent = pdfName;
  if (cardPdfView) cardPdfView.href = pdfUrl || '#';
  if (cardPdfDownload) {
    cardPdfDownload.href = pdfUrl || '#';
    cardPdfDownload.setAttribute('download', pdfName);
  }

  // Dynamic tailored pitch note adaptation
  const pitchElem = document.getElementById('apply-card-pitch');
  if (pitchElem) {
    const prof = state.profiles.find(p => p.id === state.activeProfileId) || {};
    const profName = prof.name || 'Kandidat';
    const profEdu = prof.education || 'Sarjana';
    const profGpa = prof.gpa ? ` (IPK ${prof.gpa})` : '';
    const targetRole = job.role || (detail.meta && detail.meta.role) || 'Software Engineer';
    const targetComp = job.company || (detail.meta && detail.meta.company) || 'Perusahaan';

    if (state.activeProfileId === 'damar-fikrie') {
      if (jobId.includes('sigmatech-fullstack-golang-react')) {
        pitchElem.value = `Halo Tim Rekrutmen PT Sigma Global Teknologi,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Berpengalaman membangun backend microservices berkinerja tinggi menggunakan Go (Golang) Clean Architecture dan frontend modern berbasis React.js/Next.js dan TypeScript.\n\nPortofolio nyata:\n1. Golang-Rekam — High-throughput streaming engine berbasis Go Gin, WebSocket (gorilla/websocket), dan frontend React 18 / TypeScript.\n2. Golang-Finance — RESTful API transaksi finansial menerapkan Clean Architecture dengan database PostgreSQL dan pengujian unit teruji.\n3. Dmrxai — Modern web platform interaktif berbasis Next.js 14, TypeScript, Tailwind CSS, dan Docker Compose.\n\nSaya siap berkontribusi optimal sebagai Fullstack Developer (Golang & React.js) di PT Sigma Global Teknologi.`;
      } else if (jobId.includes('talent-tech-backend-golang')) {
        pitchElem.value = `Halo Tim Rekrutmen Talent Tech,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki keahlian utama dalam backend Go (Golang) Clean Architecture, perancangan RESTful API, arsitektur microservices terdistribusi, serta pengelolaan database PostgreSQL & MySQL.\n\nPortofolio terverifikasi:\n1. Golang-Finance — RESTful API transaksi finansial menerapkan Clean Architecture (Handler -> Service -> Repository), database PostgreSQL, dan pengujian unit.\n2. Golang-Rekam — Engine backend real-time event-driven streaming berkecepatan tinggi berbasis Go Gin dan WebSockets.\n3. ServerMonitoring — Command center observabilitas multi-host Linux VPS dan deployment kontainer Docker.\n\nSaya siap bergabung segera dan berkontribusi profesional sebagai Backend Developer (Golang) di Talent Tech.`;
      } else if (jobId.includes('solusi-teknologi-kreatif')) {
        pitchElem.value = `Halo Tim Rekrutmen Solusi Teknologi Kreatif,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Berpengalaman langsung membangun platform web modern fullstack dengan backend Go (Golang) / Node.js, frontend React.js / Next.js, database PostgreSQL, serta arsitektur microservices.\n\nPortofolio nyata:\n1. Dmrxai — Multi-model web platform interaktif modern berbasis React, Next.js 14, TypeScript, Tailwind CSS, dan Docker Compose.\n2. Golang-Rekam — Streaming WebSocket engine real-time dengan frontend React 18 dan TypeScript.\n3. Golang-Finance — Arsitektur RESTful API transaksi finansial terstruktur menerapkan Clean Architecture dan integritas data ACID.\n\nSaya siap berkontribusi aktif sebagai Software Engineer di Solusi Teknologi Kreatif (Kebayoran Baru).`;
      } else if (jobId.includes('satkomindo-backend-golang')) {
        pitchElem.value = `Halo Tim Rekrutmen Pt Satkomindo Mediyasa,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki pengalaman dalam pengembangan layanan backend API dan middleware berkinerja tinggi menggunakan bahasa Go (Golang), manajemen basis data relasional (PostgreSQL & MySQL), serta administrasi server Linux VPS.\n\nPortofolio nyata:\n1. Golang-Finance — RESTful API transaksi menerapkan Clean Architecture dengan database PostgreSQL dan unit testing.\n2. Golang-Rekam — Engine streaming real-time event-driven berkecepatan tinggi berbasis Go Gin dan WebSockets.\n3. Mentari-Smart-Warehouse — Aplikasi bisnis inventaris fullstack dan manajemen database relasional dengan validasi transaksional.\n\nSaya siap hadir onsite di Jakarta Selatan dan berkontribusi optimal sebagai Backend Developer (Golang) di Pt Satkomindo Mediyasa.`;
      } else if (jobId.includes('bosshire-fullstack-engineer')) {
        pitchElem.value = `Halo Tim Rekrutmen Bosshire,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki spesialisasi utama dalam backend Go (Golang) Clean Architecture dan frontend modern berbasis TypeScript, React.js, dan Next.js (SSR).\n\nPortofolio nyata:\n1. Golang-Rekam — High-throughput streaming engine berbasis Go Gin, WebSocket (gorilla/websocket), dan frontend React 18 / TypeScript.\n2. Golang-Finance — Arsitektur RESTful API transaksi menerapkan Clean Architecture dengan database PostgreSQL dan pengujian unit teruji.\n3. Dmrxai — Modern web platform interaktif berbasis Next.js 14, TypeScript, Tailwind CSS, dan Docker Compose.\n\nSaya siap bekerja onsite di Jakarta Barat dan berkontribusi maksimal mengembangkan platform BossHire.`;
      } else if (jobId.includes('klikcair-fullstack-engineer')) {
        pitchElem.value = `Halo Tim Rekrutmen KlikCair,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki keahlian utama dalam backend Go (Golang) berkecepatan tinggi, arsitektur microservices terdistribusi, manajemen basis data relasional (MySQL / PostgreSQL), dan kepatuhan prinsip Clean Code & ACID.\n\nPortofolio terverifikasi:\n1. Golang-Finance — RESTful API transaksi finansial menerapkan Clean Architecture (Handler -> Service -> Repository), PostgreSQL, dan unit testing.\n2. Golang-Rekam — Engine backend real-time event-driven streaming berbasis Go Gin dan WebSockets.\n3. Mentari-Smart-Warehouse — Aplikasi inventaris bisnis fullstack (React.js, REST API, MySQL) dengan validasi real-time.\n\nSaya siap berkontribusi profesional membangun layanan fintech P2P lending berkinerja tinggi di KlikCair (Jakarta Barat).`;
      } else if (jobId.includes('pharos-fullstack')) {
        pitchElem.value = `Halo Tim Rekrutmen Pharos Indonesia,\n\nSaya Damar Fikrie, fresh graduate Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Menguasai pengembangan aplikasi web modern (JavaScript/TypeScript, React.js, HTML/CSS), arsitektur RESTful API, perancangan database relasional (MySQL / PostgreSQL), serta version control Git.\n\nPortofolio nyata:\n1. Mentari-Smart-Warehouse — Aplikasi web bisnis inventaris fullstack (React.js, REST API, MySQL) dengan kategorisasi dinamis dan validasi transaksional.\n2. Dmrxai — Platform aplikasi web modern interaktif berbasis React, Next.js 14, TypeScript, dan kontainer Docker.\n3. Golang-Finance — RESTful API transaksi terstruktur menerapkan Clean Architecture dan integritas data ACID.\n\nSebagai lulusan baru berprestasi yang adaptif, saya siap berkontribusi aktif sebagai Full Stack Junior Programmer di Pharos Indonesia.`;
      } else if (jobId.includes('suvarna-media')) {
        pitchElem.value = `Halo Tim Rekrutmen PT Suvarna Media Informatika,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Berpengalaman membangun aplikasi web berbasis backend PHP/Laravel dan Go, perancangan dan optimasi kueri basis data relasional PostgreSQL & MySQL, serta arsitektur RESTful API yang aman dan efisien.\n\nPortofolio relevan:\n1. Mentari-Smart-Warehouse — Aplikasi inventaris fullstack berbasis PHP, React.js, REST API, dan MySQL dengan deployment server Linux VPS.\n2. Golang-Finance — Pemodelan skema relasional PostgreSQL terindeks dan pengujian unit teruji.\n3. Dmrxai — Modern web application terintegrasi Docker dan arsitektur RESTful API.\n\nSaya siap hadir onsite di Jakarta dan berkontribusi optimal sebagai Software Engineer di PT Suvarna Media Informatika.`;
      } else if (jobId.includes('reka-multi-aptika')) {
        pitchElem.value = `Halo Tim Rekrutmen PT Reka Multi Aptika,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak (Program Analyst) dari BNSP. Berpengalaman membangun aplikasi web fullstack berskala enterprise menggunakan JavaScript/TypeScript, React.js, arsitektur RESTful API, dan database relasional (PostgreSQL & MySQL).\n\nPortofolio nyata:\n1. Dmrxai — Platform aplikasi web interaktif modern berbasis React, Next.js 14, TypeScript, dan arsitektur RESTful API terintegrasi Docker.\n2. Mentari-Smart-Warehouse — Aplikasi inventaris fullstack (React.js, REST API, MySQL) dengan penomoran barang otomatis dan validasi real-time.\n3. Golang-Finance — Arsitektur RESTful API transaksi menerapkan Clean Architecture dengan database PostgreSQL dan unit testing.\n\nSaya siap hadir onsite di Jakarta Pusat dan berkontribusi optimal sebagai Software Engineer (Fullstack) di PT Reka Multi Aptika.`;
      } else if (jobId.includes('eka-nusantara-gemilang')) {
        pitchElem.value = `Halo Tim Rekrutmen PT Eka Nusantara Gemilang (1ENGAGE),\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki keahlian utama dalam backend Go (Golang) berkecepatan tinggi, arsitektur microservices, manajemen database PostgreSQL, kontainerisasi Docker, serta frontend modern TypeScript.\n\nPortofolio terverifikasi:\n1. Golang-Rekam — High-throughput streaming engine berbasis Go Gin, WebSocket (gorilla/websocket), dan frontend React 18 / TypeScript.\n2. Golang-Finance — Arsitektur backend transaksi finansial menerapkan Clean Architecture dengan database PostgreSQL dan integritas ACID.\n3. Dmrxai — Multi-model AI web platform interaktif berbasis TypeScript, Tailwind CSS, dan Docker Compose.\n\nSaya siap berkontribusi profesional mengembangkan platform messaging omnichannel 1ENGAGE di Jakarta.`;
      } else if (jobId.includes('raja-cepat-nusantara')) {
        pitchElem.value = `Halo Tim Rekrutmen PT Raja Cepat Nusantara (Eureka Group),\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki pengalaman langsung membangun aplikasi web inventaris dan manajemen operasional bisnis berbasis React.js, Node.js, dan database MySQL/PostgreSQL, serta administrasi server Linux VPS.\n\nPortofolio nyata:\n1. Mentari-Smart-Warehouse — Aplikasi bisnis inventaris fullstack (React.js, REST API, MySQL) dengan kategorisasi dinamis dan validasi transaksional.\n2. Dmrxai — Platform web interaktif modern berbasis React, Next.js 14, dan TypeScript dengan arsitektur RESTful API.\n3. ServerMonitoring — Observabilitas multi-host Linux VPS, telemetri real-time, dan manajemen proses Nginx / Docker.\n\nSebagai lulusan baru dengan portofolio web nyata yang solid, saya siap berkontribusi penuh sebagai Staff IT Full Stack Web Developer di Eureka Group.`;
      } else if (jobId.includes('sigmatech-software-developer-golang')) {
        pitchElem.value = `Halo Tim Rekrutmen PT Sigma Global Teknologi,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak (Program Analyst) dari BNSP. Berpengalaman membangun layanan backend microservices berkinerja tinggi menggunakan Go (Golang) Clean Architecture, manajemen database PostgreSQL, perancangan RESTful API aman, serta kontainerisasi Docker.\n\nPortofolio nyata:\n1. Golang-Finance — RESTful API transaksi finansial menerapkan Clean Architecture (Handler -> Service -> Repository), database PostgreSQL, dan pengujian unit.\n2. Golang-Rekam — Backend streaming real-time berkecepatan tinggi berbasis Go Gin dan WebSocket.\n3. ServerMonitoring — Command center observabilitas server Linux VPS dan deployment kontainer Docker.\n\nSaya siap bergabung segera (ASAP) dan berkontribusi optimal sebagai Golang Developer di PT Sigma Global Teknologi.`;
      } else if (jobId.includes('entrust-digital')) {
        pitchElem.value = `Halo Tim Rekrutmen Entrepreneur Trust Digital (Entrust Digital),\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak (Program Analyst) dari BNSP. Berpengalaman membangun aplikasi web responsif modern berbasis React.js & TypeScript, layanan backend RESTful API Node.js & Go, perancangan database PostgreSQL/MySQL, serta kontainerisasi Docker.\n\nPortofolio nyata:\n1. Dmrxai — Platform aplikasi web interaktif berbasis React, Next.js 14, TypeScript, dan arsitektur RESTful API.\n2. Mentari-Smart-Warehouse — Aplikasi bisnis inventaris fullstack (React.js, REST API, MySQL) dengan penomoran barang otomatis dan validasi real-time.\n3. Golang-Finance — RESTful API transaksi finansial menerapkan Clean Architecture dengan database PostgreSQL dan pengujian unit.\n\nSaya siap bergabung segera (ASAP) dan berkontribusi optimal untuk proyek perbankan (Bank BRI) di Entrust Digital.`;
      } else if (jobId.includes('avows-technologies')) {
        pitchElem.value = `Halo Tim Rekrutmen PT Avows Technologies,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki spesialisasi dalam frontend modern Next.js/React.js, arsitektur RESTful API berkinerja tinggi, pemodelan dan optimasi database relasional (PostgreSQL & MySQL), serta pemahaman kuat mengenai SDLC dan version control Git.\n\nPortofolio nyata:\n1. Dmrxai — Multi-model web platform interaktif berbasis Next.js 14, TypeScript, Tailwind CSS, dan Docker Compose.\n2. Golang-Rekam — Dashboard pengawasan real-time dengan frontend React 18, Vite, TypeScript, dan WebSockets.\n3. Golang-Finance — Arsitektur RESTful API keuangan menerapkan Clean Architecture dengan database relasional terstruktur.\n\nSaya siap berkontribusi profesional sebagai Fullstack Developer di PT Avows Technologies (Menara Rajawali).`;
      } else if (jobId.includes('flin-fullstack')) {
        pitchElem.value = `Halo Tim Rekrutmen FLIN,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Resmi Pengembang Perangkat Lunak dari BNSP. Berpengalaman langsung mengintegrasikan layanan AI API multi-model, membangun backend RESTful API Node.js & Go, perancangan frontend interaktif React.js/Next.js, serta administrasi server Linux VPS dan kontainer Docker.\n\nPortofolio relevan:\n1. Dmrxai — Multi-model AI web platform interaktif mengintegrasikan berbagai API LLM dan pemrosesan data asinkron.\n2. Auto-Subtitle-AI — Backend automasi pengolahan data multimedia asinkron berbasis Python FastAPI dan pipeline Docker.\n3. ServerMonitoring — Command center observabilitas multi-host Linux VPS, telemetri real-time, dan manajemen proses Nginx.\n\nSaya siap bekerja onsite di Jakarta Selatan dan berkontribusi aktif mengembangkan produk digital inovatif di FLIN.`;
      } else if (jobId.includes('iquartz-junior')) {
        pitchElem.value = `Halo Tim Rekrutmen iQuartz Pte Ltd,\n\nSaya Damar Fikrie, Sarjana Komputer (Cum Laude, IPK 3.85 / 4.00) dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak (Program Analyst) dari BNSP. Menguasai prinsip OOP, penulisan clean code yang mudah dipelihara, perancangan RESTful API, pemodelan database SQL, serta version control Git.\n\nPortofolio terverifikasi:\n1. Golang-Finance — RESTful API modular menerapkan Clean Architecture (Handler -> Service -> Repository) dan database PostgreSQL.\n2. Dmrxai — Platform aplikasi web modern interaktif berbasis Next.js, React, TypeScript, dan Docker Compose.\n3. ServerMonitoring — Command center observabilitas server Linux dan deployment kontainer Docker.\n\nSebagai lulusan baru berprestasi yang adaptif dan berorientasi pada detail, saya siap berkontribusi aktif sebagai Junior Software Engineer di iQuartz Pte Ltd.`;
      } else {
        pitchElem.value = `Halo Tim Rekrutmen ${targetComp},\n\nSaya ${profName}, ${profEdu}${profGpa} dengan Sertifikasi Kompetensi Pengembang Perangkat Lunak dari BNSP. Memiliki portofolio nyata: Go WebSocket streaming (Golang-Rekam), platform fullstack Mentari Smart Warehouse, dan AI Auto Subtitle.\n\nSaya siap berkontribusi profesional untuk posisi ${targetRole} di ${targetComp}. Berkas CV tersesuaikan telah terlampir.`;
      }
    } else {
      const skillsStr = (prof.skills && prof.skills.length > 0) ? prof.skills.slice(0, 4).join(', ') : 'keahlian teknis terkait';
      pitchElem.value = `Halo Tim Rekrutmen ${targetComp},\n\nSaya ${profName}, lulusan ${profEdu}${profGpa} yang memiliki fokus keahlian di bidang ${prof.industry || 'teknis'}. Terbiasa menggunakan tools ${skillsStr} serta menyusun dokumen teknis standar industri.\n\nSaya siap berkontribusi optimal untuk posisi ${targetRole} di ${targetComp}. Portofolio dan rekam karya terlampir lengkap pada berkas CV.`;
    }
  }

  // Workflow Steps and Pipeline Tracker
  const step1Box = document.getElementById('step-1-box');
  const step2Box = document.getElementById('step-2-box');
  const btnStartApply = document.getElementById('btn-start-apply');
  const btnConfirmSubmitted = document.getElementById('btn-confirm-submitted');
  const skipBtn = document.getElementById('btn-skip-job');
  const stagePill = document.getElementById('detail-stage-pill');
  const stageSelect = document.getElementById('pipeline-stage-select');
  const notesInput = document.getElementById('pipeline-notes-input');

  if (stageSelect) stageSelect.value = job.status || 'pending_review';
  if (notesInput) notesInput.value = job.notes || '';

  // Update Status Pill
  if (stagePill) {
    stagePill.className = `stage-pill-current ${job.status || 'pending_review'}`;
    stagePill.textContent = (job.status || 'PENDING_REVIEW').replace(/_/g, ' ').toUpperCase();
  }

  // Reset steps highlight
  if (step1Box) step1Box.classList.remove('active', 'completed');
  if (step2Box) step2Box.classList.remove('active', 'completed');

  if (job.status === 'pending_review') {
    if (step1Box) step1Box.classList.add('active');
    if (btnStartApply) btnStartApply.disabled = false;
    if (btnConfirmSubmitted) btnConfirmSubmitted.disabled = true;
    if (skipBtn) {
      skipBtn.style.display = 'inline-flex';
      skipBtn.textContent = 'Lewati Lowongan Ini';
    }
  } else if (job.status === 'ready_to_submit') {
    if (step1Box) step1Box.classList.add('completed');
    if (step2Box) step2Box.classList.add('active');
    if (btnStartApply) btnStartApply.disabled = false;
    if (btnConfirmSubmitted) btnConfirmSubmitted.disabled = false;
    if (skipBtn) {
      skipBtn.style.display = 'inline-flex';
      skipBtn.textContent = 'Lewati Lowongan Ini';
    }
  } else if (job.status === 'applied' || ['screening', 'test_assigned', 'interview_hr', 'interview_tech', 'offered'].includes(job.status)) {
    if (step1Box) step1Box.classList.add('completed');
    if (step2Box) step2Box.classList.add('completed');
    if (btnStartApply) btnStartApply.disabled = false;
    if (btnConfirmSubmitted) btnConfirmSubmitted.disabled = true;
    if (skipBtn) skipBtn.style.display = 'none';
  } else if (job.status === 'skipped') {
    if (skipBtn) {
      skipBtn.style.display = 'inline-flex';
      skipBtn.textContent = 'Kembalikan ke Antrean';
    }
  }

  // Render Panes Content
  const etabReadme = document.getElementById('etab-readme');
  const etabGap = document.getElementById('etab-gap');
  const etabJob = document.getElementById('etab-job');
  const yamlEditor = document.getElementById('detail-yaml-editor');

  if (etabReadme) etabReadme.innerHTML = parseMarkdown(detail.readme_md);
  if (etabGap) etabGap.innerHTML = parseMarkdown(detail.gap_report_md);
  if (etabJob) etabJob.innerHTML = parseMarkdown(detail.job_md);
  if (yamlEditor) yamlEditor.value = detail.cv_yaml || '';
}

// ==========================================================================
// 5. ACTION BUTTONS & EVENT HANDLERS
// ==========================================================================

function setupActionButtons() {
  // Step 1: Open Portal & Copy Pitch
  const btnStartApply = document.getElementById('btn-start-apply');
  if (btnStartApply) {
    btnStartApply.addEventListener('click', async () => {
      if (!state.activeJobId) return;
      const pitchElem = document.getElementById('apply-card-pitch');
      if (pitchElem && pitchElem.value) {
        try {
          await navigator.clipboard.writeText(pitchElem.value);
        } catch (err) {}
      }

      const res = await apiPost('/api/action', {
        action: 'start_apply',
        job_id: state.activeJobId
      });

      if (res && res.success) {
        showToast('🚀 Portal dibuka! Cover note & pitch tersalin ke clipboard.', 'success');
        await loadStats();
        await loadJobs();
      }
    });
  }

  // Step 2: Confirm Submitted
  const btnConfirmSubmitted = document.getElementById('btn-confirm-submitted');
  if (btnConfirmSubmitted) {
    btnConfirmSubmitted.addEventListener('click', async () => {
      if (!state.activeJobId) return;
      const notesInput = document.getElementById('pipeline-notes-input');
      const notes = notesInput ? notesInput.value : '';

      const res = await apiPost('/api/action', {
        action: 'confirm_submitted',
        job_id: state.activeJobId,
        notes: notes
      });

      if (res && res.success) {
        showToast(res.message, 'success');
        await loadStats();
        await loadJobs();
      }
    });
  }

  // Skip / Unskip Button
  const btnSkip = document.getElementById('btn-skip-job');
  if (btnSkip) {
    btnSkip.addEventListener('click', async () => {
      if (!state.activeJobId) return;
      const current = state.jobs.find(j => j.job_id === state.activeJobId);
      if (!current) return;

      const isSkipped = current.status === 'skipped';
      const action = isSkipped ? 'unskip' : 'skip';

      const res = await apiPost('/api/action', {
        action: action,
        job_id: state.activeJobId,
        reason: 'Dilewati oleh pengguna via Dashboard'
      });

      if (res && res.success) {
        showToast(res.message, 'info');
        await loadStats();
        await loadJobs();
      }
    });
  }

  // Save Pipeline Status Change
  const btnSaveStage = document.getElementById('btn-save-stage');
  if (btnSaveStage) {
    btnSaveStage.addEventListener('click', async () => {
      if (!state.activeJobId) return;
      const stageSelect = document.getElementById('pipeline-stage-select');
      const notesInput = document.getElementById('pipeline-notes-input');

      const newStage = stageSelect ? stageSelect.value : 'screening';
      const notes = notesInput ? notesInput.value : '';

      const res = await apiPost('/api/action', {
        action: 'update_stage',
        job_id: state.activeJobId,
        stage: newStage,
        notes: notes
      });

      if (res && res.success) {
        showToast(res.message, 'success');
        await loadStats();
        await loadJobs();
      }
    });
  }

  // Open Folder in Finder
  const btnOpenFinder = document.getElementById('btn-open-finder');
  if (btnOpenFinder) {
    btnOpenFinder.addEventListener('click', async () => {
      if (!state.activeJobId) return;
      const res = await apiPost('/api/action', {
        action: 'open_folder',
        job_id: state.activeJobId
      });

      if (res && res.success) {
        showToast(res.message, 'success');
      }
    });
  }

  // Copy Folder Path Button
  const btnCopyPath = document.getElementById('btn-copy-path');
  if (btnCopyPath) {
    btnCopyPath.addEventListener('click', async () => {
      const folderEl = document.getElementById('apply-card-folder-display');
      const pathText = folderEl ? (folderEl.getAttribute('data-full-path') || folderEl.textContent.trim()) : '';
      if (pathText) {
        try {
          await navigator.clipboard.writeText(pathText);
          showToast('Path folder berhasil disalin ke clipboard!', 'success');
        } catch (e) {
          showToast(pathText, 'info');
        }
      }
    });
  }

  // Re-Render CV Yaml Instantly via RenderCV
  const btnRerender = document.getElementById('btn-rerender-yaml');
  if (btnRerender) {
    btnRerender.addEventListener('click', async () => {
      if (!state.activeJobId) {
        showToast('Pilih lowongan terlebih dahulu', 'warning');
        return;
      }
      const yamlContent = document.getElementById('detail-yaml-editor')?.value || '';
      showToast('Mengompilasi ulang PDF CV via RenderCV...', 'info');
      btnRerender.disabled = true;

      const res = await apiPost('/api/rerender', {
        job_id: state.activeJobId,
        cv_yaml: yamlContent
      });

      btnRerender.disabled = false;
      if (res && res.success) {
        showToast(res.message, 'success');
        const iframe = document.getElementById('detail-pdf-frame');
        if (iframe) iframe.src = `${res.pdf_url}#toolbar=1`;
        const viewLink = document.getElementById('apply-card-pdf-view');
        if (viewLink) viewLink.href = res.pdf_url;
        const dlLink = document.getElementById('apply-card-pdf-download');
        if (dlLink) dlLink.href = res.pdf_url;
      } else {
        showToast((res && res.error) || 'Gagal kompilasi PDF', 'error');
      }
    });
  }

  // Refresh PDF Iframe Button
  const btnRefreshPdf = document.getElementById('etab-pdf-refresh');
  if (btnRefreshPdf) {
    btnRefreshPdf.addEventListener('click', () => {
      if (!state.activeJobId) return;
      const iframe = document.getElementById('detail-pdf-frame');
      if (iframe && iframe.src) {
        const baseSrc = iframe.src.split('?')[0].split('#')[0];
        iframe.src = `${baseSrc}?t=${Date.now()}#toolbar=1`;
        showToast('Pratinjau PDF disegarkan', 'info');
      }
    });
  }

  // Refresh Activity Log Button
  const btnRefreshLogs = document.getElementById('btn-refresh-logs');
  if (btnRefreshLogs) {
    btnRefreshLogs.addEventListener('click', async () => {
      await loadLogs();
      showToast('Log aktivitas disegarkan', 'info');
    });
  }
}

// ==========================================================================
// 6. SETUP EDITORIAL TABS (DETAIL VIEW PANES)
// ==========================================================================

function setupEditorialTabs() {
  const tabs = document.querySelectorAll('.e-tab-btn');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.e-pane').forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      const targetPaneId = tab.getAttribute('data-etab');
      const targetPane = document.getElementById(targetPaneId);
      if (targetPane) targetPane.classList.add('active');
    });
  });
}

// ==========================================================================
// 7. SETUP BOARD FILTERS & SEARCH
// ==========================================================================

function setupFilters() {
  const searchInput = document.getElementById('board-search');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.searchTerm = e.target.value;
      renderMasterJobList();
    });
  }

  const catPills = document.querySelectorAll('.filter-pill');
  catPills.forEach(pill => {
    pill.addEventListener('click', () => {
      catPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      state.filterCategory = pill.getAttribute('data-cat');
      renderMasterJobList();
    });
  });

  const locSelect = document.getElementById('board-location-filter');
  if (locSelect) {
    locSelect.addEventListener('change', (e) => {
      state.filterLocation = e.target.value;
      renderMasterJobList();
    });
  }

  const statusSelect = document.getElementById('board-status-filter');
  if (statusSelect) {
    statusSelect.addEventListener('change', (e) => {
      state.filterStatus = e.target.value;
      renderMasterJobList();
    });
  }

  // Header metric status click
  document.querySelectorAll('.h-metric[data-filter-status]').forEach(metric => {
    metric.addEventListener('click', () => {
      document.querySelectorAll('.h-metric').forEach(m => m.classList.remove('active'));
      metric.classList.add('active');

      state.filterStatus = metric.getAttribute('data-filter-status');
      if (statusSelect) statusSelect.value = state.filterStatus;
      const boardTab = document.querySelector('.nav-tab-btn[data-tab="tab-board"]');
      if (boardTab) boardTab.click();
      renderMasterJobList();
    });
  });
}

// ==========================================================================
// 8. SETUP SCRAPER DRAWER
// ==========================================================================

function setupScraperDrawer() {
  const btnToggle = document.getElementById('btn-toggle-scraper');
  const btnClose = document.getElementById('btn-close-scraper');
  const drawer = document.getElementById('quick-scraper-box');
  const form = document.getElementById('scanner-form');

  if (btnToggle && drawer) {
    btnToggle.addEventListener('click', () => {
      drawer.style.display = drawer.style.display === 'none' ? 'block' : 'none';
    });
  }

  if (btnClose && drawer) {
    btnClose.addEventListener('click', () => {
      drawer.style.display = 'none';
    });
  }

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const keyword = document.getElementById('scan-keyword')?.value?.trim() || '';
      const location = document.getElementById('scan-location')?.value || 'Semua Wilayah';
      const source = document.getElementById('scan-source')?.value || 'Glints Indonesia';

      if (!keyword) {
        showToast('Kata kunci lowongan wajib diisi', 'warning');
        return;
      }

      showToast(`Menjalankan scraper untuk "${keyword}"...`, 'info');
      const res = await apiPost('/api/search', { keyword, location, source });
      if (res && res.success) {
        showToast(res.message, 'success');
        if (drawer) drawer.style.display = 'none';
      }
    });
  }
}

// ==========================================================================
// 9. LOAD PROJECTS PORTFOLIO
// ==========================================================================

async function loadProjects() {
  const projects = await apiGet('/api/projects');
  state.projects = projects || [];

  const container = document.getElementById('projects-container');
  if (!container) return;
  container.innerHTML = '';

  if (!projects || projects.length === 0) {
    container.innerHTML = `
      <div class="empty-state-box glass-panel" style="grid-column: 1 / -1; padding: 40px; text-align: center;">
        <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>
        <h3 style="margin-top: 14px; font-size: 16px; color: var(--text-heading);">Belum Ada Proyek Terdaftar</h3>
        <p style="font-size: 13px; color: var(--text-dim); margin-top: 6px;">Data rekam karya atau portofolio untuk profil ini belum dicatat di <code>master.yaml</code>.</p>
      </div>
    `;
    return;
  }

  projects.forEach(proj => {
    const card = document.createElement('div');
    card.className = 'project-card glass-panel';

    const techList = proj.tech_stack || proj.tech || [];
    const techTags = techList.map(t => `<span class="tech-tag">${escapeHtml(t)}</span>`).join('');
    const repoUrl = proj.repo_url || proj.url || '';
    const repoLink = repoUrl && !repoUrl.includes('Private')
      ? `<a href="${escapeHtml(repoUrl)}" target="_blank" class="repo-link">Tautan Proyek ↗</a>`
      : (repoUrl.includes('Private') ? `<span class="repo-link text-dim">Private Repo</span>` : '');

    let desc = proj.description || '';
    if (!desc && proj.facts && proj.facts.length > 0) {
      desc = proj.facts[0].hasil || proj.facts[0].aksi || '';
    }
    if (!desc && proj.role) {
      desc = `Peran: ${proj.role}`;
    }

    card.innerHTML = `
      <div class="project-card-header">
        <h3 class="project-title">${escapeHtml(proj.name)}</h3>
        ${repoLink}
      </div>
      <div style="font-size: 12px; color: var(--accent-cyan); font-weight: 500; margin-bottom: 8px;">${escapeHtml(proj.role || 'Contributor')}</div>
      <p class="project-desc">${escapeHtml(desc)}</p>
      <div class="project-tech-tags">${techTags}</div>
    `;
    container.appendChild(card);
  });
}

// ==========================================================================
// 10. LOAD AUDIT LOGS
// ==========================================================================

async function loadLogs() {
  const logs = await apiGet('/api/logs');
  if (!logs) return;
  state.logs = logs;

  const tbody = document.getElementById('logs-tbody');
  if (!tbody) return;
  tbody.innerHTML = '';

  logs.forEach(log => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td style="font-family: var(--font-mono); font-size: 11px; color: var(--text-dim);">${escapeHtml(log.timestamp)}</td>
      <td><code>${escapeHtml(log.job_id)}</code></td>
      <td><strong>${escapeHtml(log.company)}</strong></td>
      <td>${escapeHtml(log.role)}</td>
      <td><span class="tag-badge violet">${escapeHtml(log.event)}</span></td>
      <td><span class="tag-badge">${escapeHtml(log.channel)}</span></td>
      <td>${escapeHtml(log.detail)}</td>
      <td><span class="tag-badge emerald">${escapeHtml(log.next_action)}</span></td>
    `;
    tbody.appendChild(tr);
  });
}

// ==========================================================================
// 11. SETUP NAVIGATION TABS
// ==========================================================================

function setupNavigation() {
  const tabs = document.querySelectorAll('.nav-tab-btn');
  tabs.forEach(tab => {
    tab.addEventListener('click', async () => {
      tabs.forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));

      tab.classList.add('active');
      const targetId = tab.getAttribute('data-tab');
      const targetView = document.getElementById(targetId);
      if (targetView) targetView.classList.add('active');

      // Auto-load Drive Explorer when its tab is activated
      if (targetId === 'tab-explorer') {
        await loadExplorer(state.explorerPath || '');
      }
    });
  });
}
