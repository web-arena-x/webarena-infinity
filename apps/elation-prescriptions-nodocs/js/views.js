/* Elation Prescriptions — View Renderers */
const Views = (function() {

    function renderSidebar() {
        const pendingCount = AppState.getPendingRefillCount();
        const currentView = AppState.get('currentView');
        const items = [
            { id: 'medications', icon: '&#128138;', label: 'Active Medications', badge: null },
            { id: 'prescribe', icon: '&#9998;', label: 'Prescribe New', badge: null },
            { id: 'refills', icon: '&#128229;', label: 'Refill Requests', badge: pendingCount > 0 ? pendingCount : null },
            { id: 'history', icon: '&#128197;', label: 'Medication History', badge: null },
            { id: 'interactions', icon: '&#9888;', label: 'Interaction Checker', badge: null },
            { id: 'settings', icon: '&#9881;', label: 'Settings', badge: null }
        ];
        return items.map(item => `
            <div class="nav-item${currentView === item.id ? ' active' : ''}" data-route="${item.id}">
                <span class="nav-icon">${item.icon}</span>
                <span class="nav-label">${item.label}</span>
                ${item.badge ? `<span class="nav-badge">${item.badge}</span>` : ''}
            </div>
        `).join('');
    }

    function renderContent() {
        const view = AppState.get('currentView');
        switch (view) {
            case 'medications': return renderMedicationList();
            case 'prescribe': return renderPrescribeForm();
            case 'prescription-detail': return renderPrescriptionDetail();
            case 'refills': return renderRefillRequests();
            case 'history': return renderMedicationHistory();
            case 'interactions': return renderInteractionChecker();
            case 'settings': return renderSettings();
            default: return renderMedicationList();
        }
    }

    // ==================== MEDICATION LIST ====================
    function renderMedicationList() {
        const patient = AppState.getCurrentPatient();
        const prescriptions = AppState.getFilteredPrescriptions();
        const filter = AppState.get('medicationFilter');
        const sort = AppState.get('medicationSort');
        const searchQuery = AppState.get('searchQuery');

        const filterOptions = [
            { value: 'active', label: 'Active' },
            { value: 'all', label: 'All' },
            { value: 'discontinued', label: 'Discontinued' },
            { value: 'completed', label: 'Completed' }
        ];

        const sortOptions = [
            { value: 'name-asc', label: 'Name (A-Z)' },
            { value: 'name-desc', label: 'Name (Z-A)' },
            { value: 'date-desc', label: 'Newest First' },
            { value: 'date-asc', label: 'Oldest First' },
            { value: 'status', label: 'Status' }
        ];

        return `
            ${Components.patientHeader(patient)}
            <div class="content-header">
                <h2>Medications</h2>
                <button class="btn btn-primary" data-action="new-prescription">+ New Prescription</button>
            </div>
            <div class="filter-bar">
                <div class="filter-tabs">
                    ${filterOptions.map(f => `<button class="filter-tab${filter === f.value ? ' active' : ''}" data-action="set-med-filter" data-value="${f.value}">${f.label}</button>`).join('')}
                </div>
                <div class="filter-controls">
                    <input type="text" class="search-input" id="med-search" placeholder="Search medications..." value="${Components.escapeAttr(searchQuery)}" data-action="search-medications">
                    <div class="custom-dropdown sort-dropdown" id="med-sort-dropdown" data-dropdown-trigger="med-sort-dropdown">
                        <div class="dropdown-trigger" data-dropdown-trigger="med-sort-dropdown">
                            <span class="dropdown-text">Sort: ${sortOptions.find(s => s.value === sort)?.label || 'Name'}</span>
                            <span class="dropdown-arrow">&#9662;</span>
                        </div>
                        <div class="dropdown-menu" id="med-sort-dropdown-menu">
                            ${sortOptions.map(s => `<div class="dropdown-item${sort === s.value ? ' selected' : ''}" data-dropdown-item="med-sort-dropdown" data-value="${s.value}">${s.label}</div>`).join('')}
                        </div>
                    </div>
                </div>
            </div>
            <div class="medication-table">
                ${prescriptions.length === 0 ? Components.emptyState('&#128138;', 'No medications found') :
                `<table class="data-table">
                    <thead>
                        <tr>
                            <th>Medication</th>
                            <th>Sig / Directions</th>
                            <th>Prescriber</th>
                            <th>Start Date</th>
                            <th>Refills</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${prescriptions.map(rx => _renderMedicationRow(rx)).join('')}
                    </tbody>
                </table>`}
            </div>`;
    }

    function _renderMedicationRow(rx) {
        const provider = AppState.getProviderById(rx.prescriberId);
        const providerName = provider ? `${provider.lastName}, ${provider.firstName[0]}.` : '—';
        const drug = AppState.getDrugById(rx.drugId);
        const isControlled = drug && drug.schedule;

        return `<tr class="medication-row" data-action="view-prescription" data-rx-id="${rx.id}">
            <td class="med-name-cell">
                <div class="med-name">${Components.escapeHtml(rx.drugName)} ${rx.daw ? '<span class="daw-tag">DAW</span>' : ''} ${isControlled ? Components.scheduleBadge(drug.schedule) : ''}</div>
                <div class="med-strength">${Components.escapeHtml(rx.formStrength)}</div>
            </td>
            <td class="med-sig-cell"><div class="med-sig">${Components.escapeHtml(rx.sig)}</div></td>
            <td>${Components.escapeHtml(providerName)}</td>
            <td>${Components.formatDate(rx.startDate)}</td>
            <td>${rx.status === 'active' || rx.status === 'on-hold' ? `${rx.refillsRemaining} / ${rx.refillsTotal}` : '—'}</td>
            <td>${Components.statusBadge(rx.status)}</td>
        </tr>`;
    }

    // ==================== PRESCRIBE FORM ====================
    function renderPrescribeForm() {
        const patient = AppState.getCurrentPatient();
        const settings = AppState.get('settings');
        const formData = AppState.get('prescribeFormData') || {};

        const pharmacyOptions = AppState.get('pharmacies').map(p => ({
            value: p.id,
            label: `${p.name} (${p.type})`
        }));

        const selectedPharmacy = formData.pharmacyId || (patient ? patient.preferredPharmacy : settings.defaultPharmacy);
        const selectedDrug = formData.drugId ? AppState.getDrugById(formData.drugId) : null;

        let allergyAlerts = '';
        let interactionAlerts = '';
        if (selectedDrug) {
            const conflicts = AppState.checkAllergyConflicts(selectedDrug.id);
            allergyAlerts = Components.allergyWarning(conflicts);

            const activeDrugIds = AppState.getActivePatientDrugIds();
            if (!activeDrugIds.includes(selectedDrug.id)) {
                activeDrugIds.push(selectedDrug.id);
            }
            const interactions = AppState.checkInteractions(activeDrugIds);
            const relevantInteractions = interactions.filter(int =>
                int.drug1Id === selectedDrug.id || int.drug2Id === selectedDrug.id
            );
            interactionAlerts = Components.interactionWarning(relevantInteractions);
        }

        let formStrengthOptions = '';
        if (selectedDrug) {
            formStrengthOptions = selectedDrug.forms.map(f =>
                f.strengths.map(s => {
                    const val = `${s} ${f.form}`;
                    return `<div class="dropdown-item" data-dropdown-item="form-strength-dropdown" data-value="${Components.escapeAttr(val)}">${Components.escapeHtml(val)}</div>`;
                }).join('')
            ).join('');
        }

        let sigPresets = '';
        if (selectedDrug) {
            sigPresets = selectedDrug.commonSigs.map(s =>
                `<button class="sig-preset-btn" data-action="select-sig" data-sig="${Components.escapeAttr(s)}">${Components.escapeHtml(s)}</button>`
            ).join('');
        }

        const frequencyOptions = FREQUENCIES.map(f =>
            `<div class="dropdown-item${formData.frequency === f ? ' selected' : ''}" data-dropdown-item="frequency-dropdown" data-value="${Components.escapeAttr(f)}">${Components.escapeHtml(f)}</div>`
        ).join('');

        const routeOptions = selectedDrug
            ? selectedDrug.routes.map(r =>
                `<div class="dropdown-item${formData.route === r ? ' selected' : ''}" data-dropdown-item="route-dropdown" data-value="${Components.escapeAttr(r)}">${Components.escapeHtml(r)}</div>`
            ).join('')
            : ROUTES.map(r =>
                `<div class="dropdown-item${formData.route === r ? ' selected' : ''}" data-dropdown-item="route-dropdown" data-value="${Components.escapeAttr(r)}">${Components.escapeHtml(r)}</div>`
            ).join('');

        return `
            ${Components.patientHeader(patient)}
            <div class="content-header">
                <h2>Prescribe New Medication</h2>
            </div>
            ${allergyAlerts}
            ${interactionAlerts}
            <div class="prescribe-form" id="prescribe-form">
                <div class="form-section">
                    <h3>Drug Selection</h3>
                    <div class="form-group">
                        <label>Search Medication <span class="required">*</span></label>
                        <div class="searchable-dropdown" id="drug-search-dropdown">
                            <input type="text" class="dropdown-search-input" id="drug-search-input"
                                placeholder="Type drug name (brand or generic)..." autocomplete="off"
                                data-search-dropdown="drug-search"
                                value="${selectedDrug ? Components.escapeAttr(settings.showGenericFirst ? selectedDrug.genericName + ' (' + selectedDrug.brandName + ')' : selectedDrug.brandName + ' (' + selectedDrug.genericName + ')') : ''}">
                            <div class="dropdown-menu search-results" id="drug-search-results"></div>
                        </div>
                    </div>
                    ${selectedDrug ? `
                    <div class="selected-drug-info">
                        <div class="drug-info-row"><span class="label">Generic:</span> ${Components.escapeHtml(selectedDrug.genericName)}</div>
                        <div class="drug-info-row"><span class="label">Brand:</span> ${Components.escapeHtml(selectedDrug.brandName)}</div>
                        <div class="drug-info-row"><span class="label">Class:</span> ${Components.escapeHtml(selectedDrug.drugClass)}</div>
                        ${selectedDrug.schedule ? `<div class="drug-info-row"><span class="label">Schedule:</span> ${Components.scheduleBadge(selectedDrug.schedule)}</div>` : ''}
                    </div>` : ''}

                    ${selectedDrug ? `
                    <div class="form-group">
                        <label>Form / Strength <span class="required">*</span></label>
                        <div class="custom-dropdown" id="form-strength-dropdown" data-dropdown-trigger="form-strength-dropdown">
                            <div class="dropdown-trigger" data-dropdown-trigger="form-strength-dropdown">
                                <span class="dropdown-text">${formData.formStrength ? Components.escapeHtml(formData.formStrength) : 'Select form and strength...'}</span>
                                <span class="dropdown-arrow">&#9662;</span>
                            </div>
                            <div class="dropdown-menu" id="form-strength-dropdown-menu">${formStrengthOptions}</div>
                        </div>
                    </div>` : ''}
                </div>

                ${selectedDrug ? `
                <div class="form-section">
                    <h3>Dosing Instructions</h3>
                    <div class="form-row">
                        <div class="form-group">
                            <label for="dosage-input">Dosage</label>
                            <input type="text" id="dosage-input" class="form-input" value="${Components.escapeAttr(formData.dosage || '')}" placeholder="e.g., 20mg">
                        </div>
                        <div class="form-group">
                            <label>Frequency <span class="required">*</span></label>
                            <div class="custom-dropdown" id="frequency-dropdown" data-dropdown-trigger="frequency-dropdown">
                                <div class="dropdown-trigger" data-dropdown-trigger="frequency-dropdown">
                                    <span class="dropdown-text">${formData.frequency ? Components.escapeHtml(formData.frequency) : 'Select frequency...'}</span>
                                    <span class="dropdown-arrow">&#9662;</span>
                                </div>
                                <div class="dropdown-menu" id="frequency-dropdown-menu">${frequencyOptions}</div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label>Route <span class="required">*</span></label>
                            <div class="custom-dropdown" id="route-dropdown" data-dropdown-trigger="route-dropdown">
                                <div class="dropdown-trigger" data-dropdown-trigger="route-dropdown">
                                    <span class="dropdown-text">${formData.route ? Components.escapeHtml(formData.route) : 'Select route...'}</span>
                                    <span class="dropdown-arrow">&#9662;</span>
                                </div>
                                <div class="dropdown-menu" id="route-dropdown-menu">${routeOptions}</div>
                            </div>
                        </div>
                    </div>
                    <div class="form-row">
                        ${Components.numberInput('quantity-input', 'Quantity', formData.quantity || '', 1, 9999, 'e.g., 30')}
                        ${Components.numberInput('days-supply-input', 'Days Supply', formData.daysSupply || settings.defaultDaysSupply, 1, 365, 'e.g., 30')}
                        ${Components.numberInput('refills-input', 'Refills', formData.refills != null ? formData.refills : settings.defaultRefills, 0, 99, '0')}
                    </div>
                </div>

                <div class="form-section">
                    <h3>Directions (Sig)</h3>
                    ${sigPresets ? `<div class="sig-presets"><label>Quick presets:</label><div class="sig-preset-list">${sigPresets}</div></div>` : ''}
                    <div class="form-group">
                        <textarea id="sig-input" class="form-input form-textarea" rows="2" placeholder="Directions for patient...">${Components.escapeHtml(formData.sig || '')}</textarea>
                    </div>
                </div>

                <div class="form-section">
                    <h3>Dispensing</h3>
                    <div class="form-row">
                        <div class="form-group" style="flex:2">
                            <label>Pharmacy <span class="required">*</span></label>
                            <div class="custom-dropdown" id="pharmacy-dropdown" data-dropdown-trigger="pharmacy-dropdown">
                                <div class="dropdown-trigger" data-dropdown-trigger="pharmacy-dropdown">
                                    <span class="dropdown-text">${(() => {
                                        const ph = AppState.getPharmacyById(selectedPharmacy);
                                        return ph ? Components.escapeHtml(ph.name) : 'Select pharmacy...';
                                    })()}</span>
                                    <span class="dropdown-arrow">&#9662;</span>
                                </div>
                                <div class="dropdown-menu" id="pharmacy-dropdown-menu">
                                    ${pharmacyOptions.map(o => `<div class="dropdown-item${o.value === selectedPharmacy ? ' selected' : ''}" data-dropdown-item="pharmacy-dropdown" data-value="${Components.escapeAttr(o.value)}">${Components.escapeHtml(o.label)}</div>`).join('')}
                                </div>
                            </div>
                        </div>
                        <div class="form-group toggle-inline">
                            ${Components.toggle('daw-toggle', 'Dispense As Written (DAW)', formData.daw || false, 'Pharmacy must dispense brand name only')}
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group toggle-inline">
                            ${Components.toggle('prior-auth-toggle', 'Prior Authorization Required', formData.priorAuth || false)}
                        </div>
                        ${formData.priorAuth ? `
                        <div class="form-group">
                            <label for="prior-auth-number">PA Number</label>
                            <input type="text" id="prior-auth-number" class="form-input" value="${Components.escapeAttr(formData.priorAuthNumber || '')}" placeholder="PA number...">
                        </div>` : ''}
                    </div>
                </div>

                <div class="form-section">
                    <h3>Notes</h3>
                    <div class="form-group">
                        <textarea id="prescribe-note" class="form-input form-textarea" rows="2" placeholder="Clinical note (optional)...">${Components.escapeHtml(formData.note || '')}</textarea>
                    </div>
                </div>

                <div class="form-actions">
                    <button class="btn btn-secondary" data-action="cancel-prescribe">Cancel</button>
                    <button class="btn btn-outline" data-action="print-prescription">Print / Fax</button>
                    <button class="btn btn-primary" data-action="submit-prescription" id="submit-prescription-btn">E-Prescribe</button>
                </div>` : `
                <div class="prescribe-placeholder">
                    <p>Search for a medication above to begin prescribing.</p>
                    ${_renderFavoritesList()}
                </div>`}
            </div>`;
    }

    function _renderFavoritesList() {
        const favIds = AppState.get('settings').favoritesDrugIds || [];
        if (favIds.length === 0) return '';
        const drugs = favIds.map(id => AppState.getDrugById(id)).filter(Boolean);
        return `<div class="favorites-section">
            <h4>Favorites</h4>
            <div class="favorites-grid">
                ${drugs.map(d => `
                    <button class="favorite-drug-btn" data-action="select-favorite-drug" data-drug-id="${d.id}">
                        <div class="fav-drug-name">${Components.escapeHtml(d.genericName)}</div>
                        <div class="fav-drug-brand">${Components.escapeHtml(d.brandName)}</div>
                    </button>
                `).join('')}
            </div>
        </div>`;
    }

    // ==================== PRESCRIPTION DETAIL ====================
    function renderPrescriptionDetail() {
        const rxId = AppState.get('currentPrescriptionId');
        const rx = AppState.getPrescriptionById(rxId);
        if (!rx) return Components.emptyState('&#128196;', 'Prescription not found');

        const patient = AppState.get('patients').find(p => p.id === rx.patientId);
        const provider = AppState.getProviderById(rx.prescriberId);
        const pharmacy = AppState.getPharmacyById(rx.pharmacyId);
        const drug = AppState.getDrugById(rx.drugId);

        const providerDisplay = provider ? `${provider.title === 'MD' || provider.title === 'DO' ? 'Dr. ' : ''}${provider.firstName} ${provider.lastName}, ${provider.title}` : '—';

        return `
            ${Components.patientHeader(patient)}
            <div class="content-header">
                <div class="header-left">
                    <button class="btn btn-link" data-action="back-to-medications">&larr; Back to Medications</button>
                    <h2>${Components.escapeHtml(rx.drugName)} ${Components.escapeHtml(rx.formStrength)}</h2>
                </div>
                <div class="header-actions">
                    ${rx.status === 'active' ? `
                        <button class="btn btn-primary" data-action="renew-prescription" data-rx-id="${rx.id}">Renew</button>
                        <button class="btn btn-secondary" data-action="modify-prescription" data-rx-id="${rx.id}">Modify</button>
                        <button class="btn btn-outline" data-action="hold-prescription" data-rx-id="${rx.id}">Hold</button>
                        <button class="btn btn-danger" data-action="discontinue-prescription" data-rx-id="${rx.id}">Discontinue</button>
                    ` : ''}
                    ${rx.status === 'on-hold' ? `
                        <button class="btn btn-primary" data-action="resume-prescription" data-rx-id="${rx.id}">Resume</button>
                        <button class="btn btn-danger" data-action="discontinue-prescription" data-rx-id="${rx.id}">Discontinue</button>
                    ` : ''}
                    ${rx.status === 'discontinued' || rx.status === 'completed' ? `
                        <button class="btn btn-primary" data-action="represcribe" data-rx-id="${rx.id}">Re-prescribe</button>
                    ` : ''}
                </div>
            </div>

            <div class="detail-layout">
                <div class="detail-main">
                    <div class="detail-card">
                        <h3>Prescription Details</h3>
                        <div class="detail-grid">
                            <div class="detail-item"><span class="detail-label">Status</span><span class="detail-value">${Components.statusBadge(rx.status)}</span></div>
                            <div class="detail-item"><span class="detail-label">Drug Name</span><span class="detail-value">${Components.escapeHtml(rx.drugName)} (${Components.escapeHtml(rx.brandName)})</span></div>
                            <div class="detail-item"><span class="detail-label">Form / Strength</span><span class="detail-value">${Components.escapeHtml(rx.formStrength)}</span></div>
                            <div class="detail-item"><span class="detail-label">Directions (Sig)</span><span class="detail-value">${Components.escapeHtml(rx.sig)}</span></div>
                            <div class="detail-item"><span class="detail-label">Frequency</span><span class="detail-value">${Components.escapeHtml(rx.frequency)}</span></div>
                            <div class="detail-item"><span class="detail-label">Route</span><span class="detail-value">${Components.escapeHtml(rx.route)}</span></div>
                            <div class="detail-item"><span class="detail-label">Quantity</span><span class="detail-value">${rx.quantity}</span></div>
                            <div class="detail-item"><span class="detail-label">Days Supply</span><span class="detail-value">${rx.daysSupply}</span></div>
                            <div class="detail-item"><span class="detail-label">Refills</span><span class="detail-value">${rx.refillsRemaining} remaining of ${rx.refillsTotal}</span></div>
                            <div class="detail-item"><span class="detail-label">DAW</span><span class="detail-value">${rx.daw ? 'Yes - Dispense As Written' : 'No - Substitution Permitted'}</span></div>
                            <div class="detail-item"><span class="detail-label">Prescriber</span><span class="detail-value">${Components.escapeHtml(providerDisplay)}</span></div>
                            <div class="detail-item"><span class="detail-label">Pharmacy</span><span class="detail-value">${pharmacy ? Components.escapeHtml(pharmacy.name) : '—'}</span></div>
                            <div class="detail-item"><span class="detail-label">Start Date</span><span class="detail-value">${Components.formatDate(rx.startDate)}</span></div>
                            ${rx.endDate ? `<div class="detail-item"><span class="detail-label">End Date</span><span class="detail-value">${Components.formatDate(rx.endDate)}</span></div>` : ''}
                            ${rx.priorAuth ? `<div class="detail-item"><span class="detail-label">Prior Authorization</span><span class="detail-value">Yes — ${Components.escapeHtml(rx.priorAuthNumber || 'Pending')}</span></div>` : ''}
                            ${rx.discontinuedReason ? `<div class="detail-item"><span class="detail-label">Discontinue Reason</span><span class="detail-value">${Components.escapeHtml(rx.discontinuedReason)}</span></div>` : ''}
                            ${drug && drug.schedule ? `<div class="detail-item"><span class="detail-label">Controlled Substance</span><span class="detail-value">${Components.scheduleBadge(drug.schedule)}</span></div>` : ''}
                        </div>
                    </div>

                    <div class="detail-card">
                        <h3>Prescription History</h3>
                        <div class="history-timeline">
                            ${rx.history.map(h => `
                                <div class="history-event">
                                    <div class="history-dot ${h.action}"></div>
                                    <div class="history-content">
                                        <div class="history-action">${Components.escapeHtml(_formatHistoryAction(h.action))}</div>
                                        <div class="history-meta">
                                            ${Components.formatDate(h.date)}
                                            ${h.provider ? ` by ${Components.escapeHtml(h.provider)}` : ''}
                                            ${h.pharmacy ? ` at ${Components.escapeHtml(h.pharmacy)}` : ''}
                                        </div>
                                        ${h.note ? `<div class="history-note">${Components.escapeHtml(h.note)}</div>` : ''}
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>

                    ${rx.fillHistory.length > 0 ? `
                    <div class="detail-card">
                        <h3>Fill History</h3>
                        <table class="data-table fill-table">
                            <thead>
                                <tr><th>Fill #</th><th>Date</th><th>Pharmacy</th><th>Quantity</th><th>Days Supply</th></tr>
                            </thead>
                            <tbody>
                                ${rx.fillHistory.map(f => `
                                    <tr>
                                        <td>${f.fillNumber}</td>
                                        <td>${Components.formatDate(f.fillDate)}</td>
                                        <td>${Components.escapeHtml(f.pharmacy)}</td>
                                        <td>${f.quantity}</td>
                                        <td>${f.daysSupply}</td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>` : ''}
                </div>

                <div class="detail-sidebar">
                    ${pharmacy ? `
                    <div class="sidebar-card">
                        <h4>Pharmacy</h4>
                        <div class="pharmacy-info">
                            <div class="pharmacy-name">${Components.escapeHtml(pharmacy.name)}</div>
                            <div class="pharmacy-detail">${Components.escapeHtml(pharmacy.address)}</div>
                            <div class="pharmacy-detail">Phone: ${Components.escapeHtml(pharmacy.phone)}</div>
                            <div class="pharmacy-detail">Fax: ${Components.escapeHtml(pharmacy.fax)}</div>
                            <div class="pharmacy-detail">Type: ${Components.escapeHtml(pharmacy.type)}</div>
                            <div class="pharmacy-detail">EPCS: ${pharmacy.acceptsEPCS ? 'Yes' : 'No'}</div>
                        </div>
                    </div>` : ''}

                    <div class="sidebar-card">
                        <h4>Quick Actions</h4>
                        <div class="quick-actions">
                            ${rx.status === 'active' ? `<button class="btn btn-sm btn-outline full-width" data-action="toggle-favorite-drug" data-drug-id="${rx.drugId}">${AppState.isFavoriteDrug(rx.drugId) ? 'Remove from Favorites' : 'Add to Favorites'}</button>` : ''}
                        </div>
                    </div>
                </div>
            </div>`;
    }

    function _formatHistoryAction(action) {
        const map = {
            'prescribed': 'Prescribed',
            'filled': 'Filled by pharmacy',
            'renewed': 'Renewed',
            'modified': 'Modified',
            'discontinued': 'Discontinued',
            'on-hold': 'Placed on hold',
            'resumed': 'Resumed',
            'cancelled': 'Cancelled',
            'completed': 'Completed',
            'prior-auth-approved': 'Prior Authorization Approved',
            'refill-approved': 'Refill Approved'
        };
        return map[action] || action;
    }

    // ==================== REFILL REQUESTS ====================
    function renderRefillRequests() {
        const filter = AppState.get('refillFilter');
        const requests = AppState.getRefillRequests(filter);

        const filterOptions = [
            { value: 'pending', label: 'Pending' },
            { value: 'all', label: 'All' },
            { value: 'approved', label: 'Approved' },
            { value: 'denied', label: 'Denied' },
            { value: 'modified', label: 'Modified' }
        ];

        return `
            <div class="content-header">
                <h2>Refill Requests</h2>
            </div>
            <div class="filter-bar">
                <div class="filter-tabs">
                    ${filterOptions.map(f => `<button class="filter-tab${filter === f.value ? ' active' : ''}" data-action="set-refill-filter" data-value="${f.value}">${f.label}</button>`).join('')}
                </div>
            </div>
            <div class="refill-list">
                ${requests.length === 0 ? Components.emptyState('&#128229;', 'No refill requests') :
                requests.map(rr => _renderRefillRequestCard(rr)).join('')}
            </div>`;
    }

    function _renderRefillRequestCard(rr) {
        return `<div class="refill-card ${rr.urgency === 'urgent' ? 'urgent' : ''}">
            <div class="refill-header">
                <div class="refill-drug">${Components.escapeHtml(rr.drugName)}</div>
                <div class="refill-badges">
                    ${Components.urgencyBadge(rr.urgency)}
                    ${Components.statusBadge(rr.status)}
                </div>
            </div>
            <div class="refill-details">
                <div class="refill-detail"><span class="label">Patient:</span> ${Components.escapeHtml(rr.patientName)}</div>
                <div class="refill-detail"><span class="label">Pharmacy:</span> ${Components.escapeHtml(rr.pharmacyName)}</div>
                <div class="refill-detail"><span class="label">Requested:</span> ${Components.formatDateTime(rr.requestDate)}</div>
                <div class="refill-detail"><span class="label">Prescriber:</span> ${Components.escapeHtml(rr.originalPrescriber)}</div>
                <div class="refill-detail"><span class="label">Refills Remaining:</span> ${rr.refillsRemaining}</div>
                ${rr.notes ? `<div class="refill-notes">${Components.escapeHtml(rr.notes)}</div>` : ''}
            </div>
            ${rr.status === 'pending' ? `
            <div class="refill-actions">
                <button class="btn btn-primary btn-sm" data-action="approve-refill" data-rr-id="${rr.id}">Approve</button>
                <button class="btn btn-secondary btn-sm" data-action="modify-refill" data-rr-id="${rr.id}">Modify & Approve</button>
                <button class="btn btn-danger btn-sm" data-action="deny-refill" data-rr-id="${rr.id}">Deny</button>
            </div>` : ''}
            ${rr.status === 'denied' && rr.denyReason ? `<div class="refill-deny-reason"><strong>Reason:</strong> ${Components.escapeHtml(rr.denyReason)}</div>` : ''}
            ${rr.status === 'modified' && rr.modifiedDetails ? `<div class="refill-modified-details"><strong>Modifications:</strong> ${Components.escapeHtml(rr.modifiedDetails)}</div>` : ''}
            ${rr.responseDate ? `<div class="refill-response-date">Responded: ${Components.formatDateTime(rr.responseDate)}</div>` : ''}
        </div>`;
    }

    // ==================== MEDICATION HISTORY ====================
    function renderMedicationHistory() {
        const patient = AppState.getCurrentPatient();
        const historyFilter = AppState.get('historyFilter');
        const prescriptions = AppState.getMedicationHistory();
        const providers = AppState.get('providers');

        return `
            ${Components.patientHeader(patient)}
            <div class="content-header">
                <h2>Medication History</h2>
            </div>
            <div class="history-filters">
                <div class="form-row">
                    <div class="form-group">
                        <label for="history-date-from">From Date</label>
                        <input type="text" id="history-date-from" class="form-input" placeholder="YYYY-MM-DD" value="${Components.escapeAttr(historyFilter.dateFrom)}">
                    </div>
                    <div class="form-group">
                        <label for="history-date-to">To Date</label>
                        <input type="text" id="history-date-to" class="form-input" placeholder="YYYY-MM-DD" value="${Components.escapeAttr(historyFilter.dateTo)}">
                    </div>
                    <div class="form-group">
                        <label for="history-medication">Medication</label>
                        <input type="text" id="history-medication" class="form-input" placeholder="Search medication..." value="${Components.escapeAttr(historyFilter.medication)}">
                    </div>
                    <div class="form-group">
                        <label>Provider</label>
                        <div class="custom-dropdown" id="history-provider-dropdown" data-dropdown-trigger="history-provider-dropdown">
                            <div class="dropdown-trigger" data-dropdown-trigger="history-provider-dropdown">
                                <span class="dropdown-text">${historyFilter.provider ? Components.escapeHtml(providers.find(p => p.id === historyFilter.provider)?.lastName || 'All') : 'All Providers'}</span>
                                <span class="dropdown-arrow">&#9662;</span>
                            </div>
                            <div class="dropdown-menu" id="history-provider-dropdown-menu">
                                <div class="dropdown-item${!historyFilter.provider ? ' selected' : ''}" data-dropdown-item="history-provider-dropdown" data-value="">All Providers</div>
                                ${providers.map(p => `<div class="dropdown-item${historyFilter.provider === p.id ? ' selected' : ''}" data-dropdown-item="history-provider-dropdown" data-value="${p.id}">${Components.escapeHtml(p.lastName)}, ${Components.escapeHtml(p.firstName)} ${Components.escapeHtml(p.title)}</div>`).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="history-list">
                ${prescriptions.length === 0 ? Components.emptyState('&#128197;', 'No prescriptions found for the selected filters') :
                prescriptions.map(rx => _renderHistoryRow(rx)).join('')}
            </div>`;
    }

    function _renderHistoryRow(rx) {
        const provider = AppState.getProviderById(rx.prescriberId);
        const providerName = provider ? `${provider.lastName}, ${provider.firstName[0]}.` : '—';
        return `<div class="history-row" data-action="view-prescription" data-rx-id="${rx.id}">
            <div class="history-row-main">
                <div class="history-drug">
                    <span class="drug-name">${Components.escapeHtml(rx.drugName)}</span>
                    <span class="drug-strength">${Components.escapeHtml(rx.formStrength)}</span>
                </div>
                <div class="history-row-meta">
                    ${Components.statusBadge(rx.status)}
                    <span class="history-date">${Components.formatDate(rx.startDate)}${rx.endDate ? ` — ${Components.formatDate(rx.endDate)}` : ''}</span>
                    <span class="history-provider">${Components.escapeHtml(providerName)}</span>
                </div>
            </div>
            <div class="history-sig">${Components.escapeHtml(rx.sig)}</div>
            ${rx.discontinuedReason ? `<div class="history-dc-reason">DC Reason: ${Components.escapeHtml(rx.discontinuedReason)}</div>` : ''}
        </div>`;
    }

    // ==================== INTERACTION CHECKER ====================
    function renderInteractionChecker() {
        const checkDrugs = AppState.get('interactionCheckDrugs') || [];
        const allDrugs = checkDrugs.map(id => AppState.getDrugById(id)).filter(Boolean);
        const interactions = checkDrugs.length >= 2 ? AppState.checkInteractions(checkDrugs) : [];

        return `
            <div class="content-header">
                <h2>Drug Interaction Checker</h2>
            </div>
            <div class="interaction-checker">
                <div class="checker-input-section">
                    <div class="form-group">
                        <label>Add drugs to check interactions</label>
                        <div class="searchable-dropdown" id="interaction-drug-search">
                            <input type="text" class="dropdown-search-input" id="interaction-drug-input"
                                placeholder="Search for a drug to add..." autocomplete="off"
                                data-search-dropdown="interaction-drug-search">
                            <div class="dropdown-menu search-results" id="interaction-drug-search-results"></div>
                        </div>
                    </div>
                    ${allDrugs.length > 0 ? `
                    <div class="selected-drugs-list">
                        <h4>Selected Drugs (${allDrugs.length})</h4>
                        ${allDrugs.map(d => `
                            <div class="selected-drug-chip">
                                <span>${Components.escapeHtml(d.genericName)} (${Components.escapeHtml(d.brandName)})</span>
                                <button class="chip-remove" data-action="remove-interaction-drug" data-drug-id="${d.id}">&times;</button>
                            </div>
                        `).join('')}
                        <button class="btn btn-sm btn-outline" data-action="clear-interaction-drugs" style="margin-top:8px">Clear All</button>
                    </div>` : ''}

                    <div class="checker-preload">
                        <button class="btn btn-sm btn-secondary" data-action="load-patient-meds">Load Current Patient Medications</button>
                    </div>
                </div>

                <div class="checker-results">
                    ${checkDrugs.length < 2 ?
                        `<div class="checker-placeholder">Add at least 2 drugs to check for interactions.</div>` :
                    interactions.length === 0 ?
                        `<div class="checker-no-interactions">
                            <span class="check-icon">&#10004;</span>
                            <p>No interactions found between the selected drugs.</p>
                        </div>` :
                    `<h3>Found ${interactions.length} Interaction${interactions.length > 1 ? 's' : ''}</h3>
                    ${Components.interactionWarning(interactions)}`}
                </div>
            </div>`;
    }

    // ==================== SETTINGS ====================
    function renderSettings() {
        const settings = AppState.get('settings');
        const providers = AppState.get('providers');
        const currentProvider = AppState.getCurrentProvider();
        const pharmacies = AppState.get('pharmacies');

        const defaultPharmacy = AppState.getPharmacyById(settings.defaultPharmacy);

        return `
            <div class="content-header">
                <h2>Prescription Settings</h2>
            </div>
            <div class="settings-layout">
                <div class="settings-section">
                    <h3>Prescriber Information</h3>
                    ${currentProvider ? `
                    <div class="detail-grid">
                        <div class="detail-item"><span class="detail-label">Name</span><span class="detail-value">${Components.escapeHtml(currentProvider.firstName)} ${Components.escapeHtml(currentProvider.lastName)}, ${Components.escapeHtml(currentProvider.title)}</span></div>
                        <div class="detail-item"><span class="detail-label">Specialty</span><span class="detail-value">${Components.escapeHtml(currentProvider.specialty)}</span></div>
                        <div class="detail-item"><span class="detail-label">DEA Number</span><span class="detail-value">${Components.escapeHtml(currentProvider.deaNumber)}</span></div>
                        <div class="detail-item"><span class="detail-label">NPI</span><span class="detail-value">${Components.escapeHtml(currentProvider.npi)}</span></div>
                        <div class="detail-item"><span class="detail-label">EPCS Enrolled</span><span class="detail-value">${currentProvider.epcsEnrolled ? '<span class="status-badge" style="background:#e6f4ea;color:#137333">Enrolled</span>' : '<span class="status-badge" style="background:#fce8e6;color:#c5221f">Not Enrolled</span>'}</span></div>
                    </div>` : ''}
                </div>

                <div class="settings-section">
                    <h3>Default Pharmacy</h3>
                    <div class="form-group">
                        <div class="custom-dropdown" id="default-pharmacy-dropdown" data-dropdown-trigger="default-pharmacy-dropdown">
                            <div class="dropdown-trigger" data-dropdown-trigger="default-pharmacy-dropdown">
                                <span class="dropdown-text">${defaultPharmacy ? Components.escapeHtml(defaultPharmacy.name) : 'Select default pharmacy...'}</span>
                                <span class="dropdown-arrow">&#9662;</span>
                            </div>
                            <div class="dropdown-menu" id="default-pharmacy-dropdown-menu">
                                ${pharmacies.map(p => `<div class="dropdown-item${p.id === settings.defaultPharmacy ? ' selected' : ''}" data-dropdown-item="default-pharmacy-dropdown" data-value="${p.id}">${Components.escapeHtml(p.name)} (${Components.escapeHtml(p.type)})</div>`).join('')}
                            </div>
                        </div>
                    </div>
                </div>

                <div class="settings-section">
                    <h3>Prescribing Defaults</h3>
                    <div class="form-row">
                        ${Components.numberInput('setting-days-supply', 'Default Days Supply', settings.defaultDaysSupply, 1, 365)}
                        ${Components.numberInput('setting-refills', 'Default Refills', settings.defaultRefills, 0, 99)}
                    </div>
                    <div class="form-group">
                        <label>Prescription Print Format</label>
                        <div class="custom-dropdown" id="print-format-dropdown" data-dropdown-trigger="print-format-dropdown">
                            <div class="dropdown-trigger" data-dropdown-trigger="print-format-dropdown">
                                <span class="dropdown-text">${Components.escapeHtml(settings.printFormat.charAt(0).toUpperCase() + settings.printFormat.slice(1))}</span>
                                <span class="dropdown-arrow">&#9662;</span>
                            </div>
                            <div class="dropdown-menu" id="print-format-dropdown-menu">
                                ${PRESCRIPTION_PRINT_FORMATS.map(f => `<div class="dropdown-item${f === settings.printFormat ? ' selected' : ''}" data-dropdown-item="print-format-dropdown" data-value="${f}">${Components.escapeHtml(f.charAt(0).toUpperCase() + f.slice(1))}</div>`).join('')}
                            </div>
                        </div>
                    </div>
                </div>

                <div class="settings-section">
                    <h3>E-Prescribing Options</h3>
                    ${Components.toggle('setting-erx', 'Enable E-Prescribing', settings.eRxEnabled, 'Send prescriptions electronically to pharmacies')}
                    ${Components.toggle('setting-generic-first', 'Show Generic Name First', settings.showGenericFirst, 'Display generic drug name before brand name in search results')}
                    ${Components.toggle('setting-auto-interactions', 'Auto-Check Drug Interactions', settings.autoCheckInteractions, 'Automatically check for interactions when prescribing')}
                    ${Components.toggle('setting-allergy-review', 'Require Allergy Review', settings.requireAllergyReview, 'Show allergy alert before confirming prescription')}
                    ${Components.toggle('setting-signature', 'Require Signature', settings.signatureRequired, 'Require electronic signature for prescriptions')}
                </div>

                <div class="settings-section">
                    <h3>Formulary / Favorites</h3>
                    <p class="settings-description">Your frequently prescribed medications for quick access on the prescribe screen.</p>
                    <div class="favorites-manage-list">
                        ${(settings.favoritesDrugIds || []).map(id => {
                            const d = AppState.getDrugById(id);
                            if (!d) return '';
                            return `<div class="favorite-manage-row">
                                <span>${Components.escapeHtml(d.genericName)} (${Components.escapeHtml(d.brandName)})</span>
                                <button class="btn btn-sm btn-danger" data-action="remove-favorite" data-drug-id="${d.id}">Remove</button>
                            </div>`;
                        }).join('')}
                    </div>
                </div>

                <div class="settings-actions">
                    <button class="btn btn-primary" data-action="save-settings">Save Settings</button>
                </div>
            </div>`;
    }

    // ==================== PATIENT SELECTOR ====================
    function renderPatientSelector() {
        const currentPatient = AppState.getCurrentPatient();
        const patients = AppState.get('patients');
        if (!currentPatient) return '';
        return `<div class="patient-selector" id="patient-selector" data-dropdown-trigger="patient-selector">
            <div class="dropdown-trigger" data-dropdown-trigger="patient-selector">
                <span class="dropdown-text">${Components.escapeHtml(currentPatient.lastName)}, ${Components.escapeHtml(currentPatient.firstName)}</span>
                <span class="dropdown-arrow">&#9662;</span>
            </div>
            <div class="dropdown-menu" id="patient-selector-menu">
                ${patients.map(p => `<div class="dropdown-item${p.id === currentPatient.id ? ' selected' : ''}" data-dropdown-item="patient-selector" data-value="${p.id}">${Components.escapeHtml(p.lastName)}, ${Components.escapeHtml(p.firstName)} — ${Components.escapeHtml(p.mrn)}</div>`).join('')}
            </div>
        </div>`;
    }

    return {
        renderSidebar, renderContent, renderPatientSelector,
        renderMedicationList, renderPrescribeForm, renderPrescriptionDetail,
        renderRefillRequests, renderMedicationHistory, renderInteractionChecker, renderSettings
    };
})();
