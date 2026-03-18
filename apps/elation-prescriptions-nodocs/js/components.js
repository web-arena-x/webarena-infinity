/* Elation Prescriptions — Reusable UI Components */
const Components = (function() {

    function escapeHtml(str) {
        if (str == null) return '';
        return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    }

    function escapeAttr(str) {
        return escapeHtml(str);
    }

    function formatDate(dateStr) {
        if (!dateStr) return '—';
        const d = new Date(dateStr + (dateStr.includes('T') ? '' : 'T00:00:00'));
        return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    }

    function formatDateShort(dateStr) {
        if (!dateStr) return '—';
        const d = new Date(dateStr + (dateStr.includes('T') ? '' : 'T00:00:00'));
        return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
    }

    function formatDateTime(dateStr) {
        if (!dateStr) return '—';
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' });
    }

    function timeAgo(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        const now = new Date();
        const diffMs = now - d;
        const diffMin = Math.floor(diffMs / 60000);
        if (diffMin < 1) return 'just now';
        if (diffMin < 60) return `${diffMin}m ago`;
        const diffHr = Math.floor(diffMin / 60);
        if (diffHr < 24) return `${diffHr}h ago`;
        const diffDays = Math.floor(diffHr / 24);
        if (diffDays < 7) return `${diffDays}d ago`;
        if (diffDays < 30) return `${Math.floor(diffDays / 7)}w ago`;
        return formatDateShort(dateStr);
    }

    function statusBadge(status) {
        const colors = {
            'active': { bg: '#e6f4ea', color: '#137333', label: 'Active' },
            'discontinued': { bg: '#fce8e6', color: '#c5221f', label: 'Discontinued' },
            'on-hold': { bg: '#fef7e0', color: '#e37400', label: 'On Hold' },
            'completed': { bg: '#e8eaf6', color: '#3949ab', label: 'Completed' },
            'cancelled': { bg: '#f1f3f4', color: '#5f6368', label: 'Cancelled' },
            'pending': { bg: '#fef7e0', color: '#e37400', label: 'Pending' },
            'approved': { bg: '#e6f4ea', color: '#137333', label: 'Approved' },
            'denied': { bg: '#fce8e6', color: '#c5221f', label: 'Denied' },
            'modified': { bg: '#e8f0fe', color: '#1967d2', label: 'Modified' }
        };
        const c = colors[status] || { bg: '#f1f3f4', color: '#5f6368', label: status };
        return `<span class="status-badge" style="background:${c.bg};color:${c.color}">${escapeHtml(c.label)}</span>`;
    }

    function urgencyBadge(urgency) {
        if (urgency === 'urgent') {
            return '<span class="urgency-badge urgent">Urgent</span>';
        }
        return '<span class="urgency-badge routine">Routine</span>';
    }

    function severityBadge(severity) {
        const colors = {
            'major': { bg: '#fce8e6', color: '#c5221f' },
            'moderate': { bg: '#fef7e0', color: '#e37400' },
            'minor': { bg: '#e8f0fe', color: '#1967d2' }
        };
        const c = colors[severity] || { bg: '#f1f3f4', color: '#5f6368' };
        return `<span class="severity-badge" style="background:${c.bg};color:${c.color}">${escapeHtml(severity.charAt(0).toUpperCase() + severity.slice(1))}</span>`;
    }

    function scheduleBadge(schedule) {
        if (!schedule) return '';
        return `<span class="schedule-badge">Schedule ${escapeHtml(schedule)}</span>`;
    }

    function allergyWarning(conflicts) {
        if (!conflicts || conflicts.length === 0) return '';
        return `<div class="alert alert-danger">
            <span class="alert-icon">&#9888;</span>
            <div class="alert-content">
                <strong>Allergy Alert!</strong>
                ${conflicts.map(c => `<div class="alert-detail">${escapeHtml(c.drug)} — Patient is allergic to ${escapeHtml(c.allergen)} (${escapeHtml(c.reaction)}, severity: ${escapeHtml(c.severity)})</div>`).join('')}
            </div>
        </div>`;
    }

    function interactionWarning(interactions) {
        if (!interactions || interactions.length === 0) return '';
        return `<div class="interaction-alerts">
            ${interactions.map(int => `
                <div class="alert alert-${int.severity === 'major' ? 'danger' : int.severity === 'moderate' ? 'warning' : 'info'}">
                    <span class="alert-icon">${int.severity === 'major' ? '&#9888;' : int.severity === 'moderate' ? '&#9888;' : '&#8505;'}</span>
                    <div class="alert-content">
                        <strong>${severityBadge(int.severity)} Drug Interaction: ${escapeHtml(int.drug1Name)} + ${escapeHtml(int.drug2Name)}</strong>
                        <div class="alert-detail">${escapeHtml(int.description)}</div>
                        <div class="alert-recommendation"><strong>Recommendation:</strong> ${escapeHtml(int.recommendation)}</div>
                    </div>
                </div>
            `).join('')}
        </div>`;
    }

    function patientHeader(patient) {
        if (!patient) return '';
        const age = _calcAge(patient.dob);
        const allergyList = patient.allergies.length > 0
            ? patient.allergies.map(a => `<span class="allergy-tag ${a.severity}">${escapeHtml(a.substance)}</span>`).join('')
            : '<span class="no-allergies">NKDA (No Known Drug Allergies)</span>';
        return `<div class="patient-header">
            <div class="patient-name-row">
                <span class="patient-name">${escapeHtml(patient.lastName)}, ${escapeHtml(patient.firstName)}</span>
                <span class="patient-meta">${escapeHtml(patient.gender)} | DOB: ${formatDate(patient.dob)} (${age}y) | MRN: ${escapeHtml(patient.mrn)}</span>
            </div>
            <div class="patient-allergies-row">
                <span class="allergies-label">Allergies:</span>
                ${allergyList}
            </div>
        </div>`;
    }

    function _calcAge(dob) {
        const d = new Date(dob + 'T00:00:00');
        const now = new Date();
        let age = now.getFullYear() - d.getFullYear();
        if (now.getMonth() < d.getMonth() || (now.getMonth() === d.getMonth() && now.getDate() < d.getDate())) age--;
        return age;
    }

    function dropdown(id, label, options, selectedValue, placeholder) {
        const selected = options.find(o => o.value === selectedValue);
        const displayText = selected ? selected.label : (placeholder || 'Select...');
        return `<div class="form-group">
            ${label ? `<label>${escapeHtml(label)}</label>` : ''}
            <div class="custom-dropdown" id="${escapeAttr(id)}" data-dropdown-trigger="${escapeAttr(id)}">
                <div class="dropdown-trigger" data-dropdown-trigger="${escapeAttr(id)}">
                    <span class="dropdown-text">${escapeHtml(displayText)}</span>
                    <span class="dropdown-arrow">&#9662;</span>
                </div>
                <div class="dropdown-menu" id="${escapeAttr(id)}-menu">
                    ${options.map(o => `<div class="dropdown-item${o.value === selectedValue ? ' selected' : ''}" data-dropdown-item="${escapeAttr(id)}" data-value="${escapeAttr(o.value)}">${escapeHtml(o.label)}</div>`).join('')}
                </div>
            </div>
        </div>`;
    }

    function searchableDropdown(id, label, placeholder) {
        return `<div class="form-group">
            ${label ? `<label>${escapeHtml(label)}</label>` : ''}
            <div class="searchable-dropdown" id="${escapeAttr(id)}">
                <input type="text" class="dropdown-search-input" id="${escapeAttr(id)}-input" placeholder="${escapeAttr(placeholder || 'Search...')}" autocomplete="off" data-search-dropdown="${escapeAttr(id)}">
                <div class="dropdown-menu search-results" id="${escapeAttr(id)}-results"></div>
            </div>
        </div>`;
    }

    function textInput(id, label, value, placeholder, required) {
        return `<div class="form-group">
            <label for="${escapeAttr(id)}">${escapeHtml(label)}${required ? ' <span class="required">*</span>' : ''}</label>
            <input type="text" id="${escapeAttr(id)}" value="${escapeAttr(value || '')}" placeholder="${escapeAttr(placeholder || '')}" class="form-input"${required ? ' required' : ''}>
        </div>`;
    }

    function numberInput(id, label, value, min, max, placeholder) {
        return `<div class="form-group">
            <label for="${escapeAttr(id)}">${escapeHtml(label)}</label>
            <input type="text" inputmode="numeric" id="${escapeAttr(id)}" value="${escapeAttr(value != null ? String(value) : '')}" placeholder="${escapeAttr(placeholder || '')}" class="form-input"${min != null ? ` data-min="${min}"` : ''}${max != null ? ` data-max="${max}"` : ''}>
        </div>`;
    }

    function textarea(id, label, value, placeholder, rows) {
        return `<div class="form-group">
            <label for="${escapeAttr(id)}">${escapeHtml(label)}</label>
            <textarea id="${escapeAttr(id)}" placeholder="${escapeAttr(placeholder || '')}" class="form-input form-textarea" rows="${rows || 3}">${escapeHtml(value || '')}</textarea>
        </div>`;
    }

    function toggle(id, label, checked, description) {
        return `<div class="form-group toggle-group">
            <div class="toggle-container">
                <div class="toggle-switch${checked ? ' active' : ''}" id="${escapeAttr(id)}" data-toggle="${escapeAttr(id)}">
                    <div class="toggle-track"><div class="toggle-thumb"></div></div>
                </div>
                <label class="toggle-label" for="${escapeAttr(id)}">${escapeHtml(label)}</label>
            </div>
            ${description ? `<div class="toggle-description">${escapeHtml(description)}</div>` : ''}
        </div>`;
    }

    function showModal(title, body, footer) {
        const modal = document.getElementById('modal-overlay');
        if (!modal) return;
        modal.querySelector('.modal-title').textContent = title;
        modal.querySelector('.modal-body').innerHTML = body;
        modal.querySelector('.modal-footer').innerHTML = footer || '';
        modal.classList.add('visible');
    }

    function closeModal() {
        const modal = document.getElementById('modal-overlay');
        if (modal) modal.classList.remove('visible');
    }

    function showToast(message, type) {
        type = type || 'success';
        const container = document.getElementById('toast-container');
        if (!container) return;
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.textContent = message;
        container.appendChild(toast);
        setTimeout(() => { toast.classList.add('show'); }, 10);
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    }

    function confirm(title, message, onConfirm) {
        const body = `<p>${escapeHtml(message)}</p>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-primary" data-action="confirm-modal">Confirm</button>`;
        _confirmCallback = onConfirm;
        showModal(title, body, footer);
    }

    function confirmDanger(title, message, onConfirm) {
        const body = `<p>${escapeHtml(message)}</p>`;
        const footer = `<button class="btn btn-secondary" data-action="close-modal">Cancel</button>
                        <button class="btn btn-danger" data-action="confirm-modal">Confirm</button>`;
        _confirmCallback = onConfirm;
        showModal(title, body, footer);
    }

    let _confirmCallback = null;
    function getConfirmCallback() { return _confirmCallback; }

    function emptyState(icon, message) {
        return `<div class="empty-state">
            <div class="empty-state-icon">${icon || '&#128196;'}</div>
            <div class="empty-state-message">${escapeHtml(message)}</div>
        </div>`;
    }

    function pagination(currentPage, totalPages, totalItems) {
        if (totalPages <= 1) return '';
        let pages = '';
        const start = Math.max(1, currentPage - 2);
        const end = Math.min(totalPages, currentPage + 2);
        if (start > 1) pages += `<button class="page-btn" data-action="goto-page" data-page="1">1</button>`;
        if (start > 2) pages += `<span class="page-ellipsis">...</span>`;
        for (let i = start; i <= end; i++) {
            pages += `<button class="page-btn${i === currentPage ? ' active' : ''}" data-action="goto-page" data-page="${i}">${i}</button>`;
        }
        if (end < totalPages - 1) pages += `<span class="page-ellipsis">...</span>`;
        if (end < totalPages) pages += `<button class="page-btn" data-action="goto-page" data-page="${totalPages}">${totalPages}</button>`;

        return `<div class="pagination">
            <span class="pagination-info">Showing ${(currentPage-1) * 20 + 1}-${Math.min(currentPage * 20, totalItems)} of ${totalItems}</span>
            <div class="pagination-buttons">
                <button class="page-btn" data-action="prev-page"${currentPage <= 1 ? ' disabled' : ''}>&laquo; Prev</button>
                ${pages}
                <button class="page-btn" data-action="next-page"${currentPage >= totalPages ? ' disabled' : ''}>Next &raquo;</button>
            </div>
        </div>`;
    }

    return {
        escapeHtml, escapeAttr, formatDate, formatDateShort, formatDateTime, timeAgo,
        statusBadge, urgencyBadge, severityBadge, scheduleBadge,
        allergyWarning, interactionWarning, patientHeader,
        dropdown, searchableDropdown, textInput, numberInput, textarea, toggle,
        showModal, closeModal, showToast, confirm, confirmDanger, getConfirmCallback,
        emptyState, pagination
    };
})();
