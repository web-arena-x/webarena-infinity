/* ============================================================
   views.js — Section renderers for Elation Clinical Records
   ============================================================ */

const Views = {

    // ── Sidebar ──
    renderSidebar() {
        const sections = [
            { id: 'patients', icon: '&#128100;', label: 'Patients' },
            { id: 'templates', icon: '&#128196;', label: 'Templates' },
            { id: 'categories', icon: '&#128193;', label: 'Categories' },
            { id: 'settings', icon: '&#9881;', label: 'Settings' }
        ];
        const navItems = sections.map(s =>
            `<div class="nav-item${AppState.currentSection === s.id ? ' active' : ''}" data-action="navigate" data-section="${s.id}">
                <span class="nav-icon">${s.icon}</span>
                <span class="nav-label">${s.label}</span>
            </div>`
        ).join('');
        return `<div class="sidebar-header">
            <div class="app-logo">
                <span class="logo-icon">&#9764;</span>
                <span class="logo-text">Elation</span>
            </div>
            <div class="provider-info">
                <div class="provider-name">${Components.esc(AppState.currentProvider.fullName)}</div>
                <div class="provider-practice">${Components.esc(AppState.currentProvider.practiceName)}</div>
            </div>
        </div>
        <nav class="sidebar-nav">${navItems}</nav>`;
    },

    // ── Main Content Router ──
    renderContent() {
        switch (AppState.currentSection) {
            case 'patients': return this.renderPatients();
            case 'templates': return this.renderTemplates();
            case 'categories': return this.renderCategories();
            case 'settings': return this.renderSettings();
            default: return this.renderPatients();
        }
    },

    // ══════════════════════════════════════════════════════
    // PATIENTS SECTION
    // ══════════════════════════════════════════════════════
    renderPatients() {
        if (AppState.selectedPatientId) {
            return this.renderPatientChart();
        }
        return this.renderPatientList();
    },

    renderPatientList() {
        const query = (AppState.patientSearchQuery || '').toLowerCase();
        let patients = AppState.patients;
        if (query) {
            patients = patients.filter(p =>
                p.firstName.toLowerCase().includes(query) ||
                p.lastName.toLowerCase().includes(query) ||
                p.dateOfBirth.includes(query) ||
                (p.phone && p.phone.includes(query)) ||
                (p.insurancePrimary && p.insurancePrimary.toLowerCase().includes(query))
            );
        }
        const rows = patients.map(p => {
            const age = Components.calculateAge(p.dateOfBirth);
            const provider = AppState.getProvider(p.primaryProvider);
            const provName = provider ? provider.fullName : '';
            const tags = p.tags.map(t => Components.patientTag(t, false)).join(' ');
            return `<tr class="patient-row clickable" data-action="select-patient" data-patient-id="${p.id}">
                <td class="patient-name-cell"><strong>${Components.esc(p.lastName)}, ${Components.esc(p.firstName)}</strong></td>
                <td>${Components.esc(p.dateOfBirth)} (${age})</td>
                <td>${Components.esc(p.sexAtBirth)}</td>
                <td>${Components.esc(p.phone)}</td>
                <td>${Components.esc(provName)}</td>
                <td class="tags-cell">${tags}</td>
            </tr>`;
        }).join('');
        return `<div class="content-panel">
            ${Components.sectionHeader('Patient List', `${patients.length} patients`, '')}
            <div class="toolbar">
                ${Components.searchInput('patient-search', 'Search patients by name, DOB, phone, insurance...', AppState.patientSearchQuery)}
            </div>
            <div class="table-container">
                <table class="data-table" id="patient-table">
                    <thead><tr>
                        <th>Name</th><th>DOB (Age)</th><th>Sex</th><th>Phone</th><th>Provider</th><th>Tags</th>
                    </tr></thead>
                    <tbody>${rows}</tbody>
                </table>
            </div>
        </div>`;
    },

    // ── Patient Chart ──
    renderPatientChart() {
        const patient = AppState.getPatient(AppState.selectedPatientId);
        if (!patient) return '<div class="content-panel">Patient not found.</div>';

        const age = Components.calculateAge(patient.dateOfBirth);
        const tabs = Components.tabs([
            { id: 'chart', label: 'Clinical Profile' },
            { id: 'notes', label: 'Visit Notes' },
            { id: 'vaccinations', label: 'Vaccinations' },
            { id: 'vitals', label: 'Vitals' },
            { id: 'careplans', label: 'Care Plans' }
        ], AppState.patientTab);

        const tags = patient.tags.map(t => Components.patientTag(t, true, patient.id)).join(' ');

        let tabContent = '';
        switch (AppState.patientTab) {
            case 'chart': tabContent = this.renderClinicalProfile(patient); break;
            case 'notes': tabContent = this.renderVisitNotes(patient); break;
            case 'vaccinations': tabContent = this.renderVaccinations(patient); break;
            case 'vitals': tabContent = this.renderVitals(patient); break;
            case 'careplans': tabContent = this.renderCarePlans(patient); break;
            default: tabContent = this.renderClinicalProfile(patient);
        }

        return `<div class="content-panel">
            <div class="patient-header">
                <button class="btn btn-ghost" data-action="back-to-list">&larr; Back to Patients</button>
                <div class="patient-banner">
                    <div class="patient-avatar">${patient.firstName[0]}${patient.lastName[0]}</div>
                    <div class="patient-info">
                        <h2>${Components.esc(patient.firstName)} ${Components.esc(patient.lastName)}</h2>
                        <div class="patient-meta">
                            <span>${Components.esc(patient.dateOfBirth)} (${age} yrs)</span>
                            <span>${Components.esc(patient.sexAtBirth)}</span>
                            <span>${Components.esc(patient.insurancePrimary)} - ${Components.esc(patient.insuranceId)}</span>
                        </div>
                        <div class="patient-tags-row">${tags}
                            <button class="btn btn-xs btn-ghost" data-action="add-tag" data-patient-id="${patient.id}">+ Add Tag</button>
                        </div>
                    </div>
                </div>
            </div>
            ${tabs}
            <div class="tab-content">${tabContent}</div>
        </div>`;
    },

    // ── Clinical Profile Tab ──
    renderClinicalProfile(patient) {
        const problems = AppState.getPatientProblems(patient.id);
        const activeProblems = problems.filter(p => p.status === 'Active');
        const controlledProblems = problems.filter(p => p.status === 'Controlled');
        const resolvedProblems = problems.filter(p => p.status === 'Resolved');

        const renderProblem = (prob) => {
            const statusClass = prob.status.toLowerCase();
            const icd = prob.icd10 ? ` <span class="icd-code">${Components.esc(prob.icd10)}</span>` : '';
            return `<div class="problem-item problem-${statusClass}" data-problem-id="${prob.id}">
                <div class="problem-main">
                    <span class="problem-title">${Components.esc(prob.title)}${icd}</span>
                    <span class="problem-date">Dx: ${Components.esc(prob.dxDate)}</span>
                </div>
                ${prob.synopsis ? `<div class="problem-synopsis">${Components.esc(prob.synopsis)}</div>` : ''}
                <div class="problem-actions">
                    <button class="btn btn-xs btn-ghost" data-action="edit-problem" data-problem-id="${prob.id}">Edit</button>
                    ${prob.status === 'Active' ? `<button class="btn btn-xs btn-ghost" data-action="change-problem-status" data-problem-id="${prob.id}" data-status="Controlled">Mark Controlled</button>` : ''}
                    ${prob.status === 'Active' || prob.status === 'Controlled' ? `<button class="btn btn-xs btn-ghost" data-action="change-problem-status" data-problem-id="${prob.id}" data-status="Resolved">Mark Resolved</button>` : ''}
                    ${prob.status === 'Resolved' ? `<button class="btn btn-xs btn-ghost" data-action="change-problem-status" data-problem-id="${prob.id}" data-status="Active">Reactivate</button>` : ''}
                    ${prob.status === 'Controlled' ? `<button class="btn btn-xs btn-ghost" data-action="change-problem-status" data-problem-id="${prob.id}" data-status="Active">Mark Active</button>` : ''}
                    <button class="btn btn-xs btn-ghost" data-action="export-problem-to-note" data-problem-id="${prob.id}">Export to Note</button>
                </div>
            </div>`;
        };

        const recentVax = AppState.getPatientVaccinations(patient.id).slice(0, 3);
        const recentVaxHtml = recentVax.length > 0
            ? recentVax.map(v => `<div class="mini-item"><span>${Components.esc(v.vaccineName)}</span><span class="text-muted">${Components.formatDate(v.givenOn)}</span></div>`).join('')
            : '<div class="text-muted">No vaccinations recorded</div>';

        const recentVitals = AppState.getPatientVitals(patient.id).slice(0, 1);
        const recentVitalsHtml = recentVitals.length > 0
            ? `<div class="vitals-grid">
                ${Components.vitalValue('BP', recentVitals[0].bloodPressureSystolic ? recentVitals[0].bloodPressureSystolic + '/' + recentVitals[0].bloodPressureDiastolic : null, 'mmHg')}
                ${Components.vitalValue('HR', recentVitals[0].heartRate, 'bpm')}
                ${Components.vitalValue('Temp', recentVitals[0].temperature, recentVitals[0].temperatureUnit ? '°' + recentVitals[0].temperatureUnit : '')}
                ${Components.vitalValue('SpO2', recentVitals[0].oxygenSaturation, '%')}
                ${Components.vitalValue('Weight', recentVitals[0].weight, recentVitals[0].weightUnit)}
                ${Components.vitalValue('BMI', recentVitals[0].bmi, '')}
              </div><div class="text-muted" style="margin-top:4px">${Components.formatDate(recentVitals[0].date)}</div>`
            : '<div class="text-muted">No vitals recorded</div>';

        return `<div class="clinical-profile">
            <div class="profile-section">
                ${Components.sectionHeader('Problem List', `${problems.length} total`, Components.button('+ Add Problem', 'add-problem', 'primary'))}
                ${activeProblems.length > 0 ? `<div class="problem-group"><h4>Active (${activeProblems.length})</h4>${activeProblems.map(renderProblem).join('')}</div>` : ''}
                ${controlledProblems.length > 0 ? `<div class="problem-group"><h4>Controlled (${controlledProblems.length})</h4>${controlledProblems.map(renderProblem).join('')}</div>` : ''}
                ${resolvedProblems.length > 0 ? `<div class="problem-group"><h4>Resolved (${resolvedProblems.length})</h4>${resolvedProblems.map(renderProblem).join('')}</div>` : ''}
                ${problems.length === 0 ? Components.emptyState('No problems documented yet.', Components.button('+ Add Problem', 'add-problem', 'primary')) : ''}
            </div>
            <div class="profile-columns">
                <div class="profile-section profile-section-sm">
                    <h3>Recent Vaccinations</h3>
                    ${recentVaxHtml}
                    <button class="btn btn-xs btn-link" data-action="switch-tab" data-tab="vaccinations">View All</button>
                </div>
                <div class="profile-section profile-section-sm">
                    <h3>Latest Vitals</h3>
                    ${recentVitalsHtml}
                    <button class="btn btn-xs btn-link" data-action="switch-tab" data-tab="vitals">View All / Add Historical</button>
                </div>
            </div>
            <div class="profile-section">
                <h3>Demographics</h3>
                <div class="demographics-grid">
                    <div class="demo-item"><label>Legal Name</label><span>${Components.esc(patient.legalFirstName)} ${Components.esc(patient.legalLastName)}</span></div>
                    <div class="demo-item"><label>Date of Birth</label><span>${Components.esc(patient.dateOfBirth)}</span></div>
                    <div class="demo-item"><label>Sex at Birth</label><span>${Components.esc(patient.sexAtBirth)}</span></div>
                    <div class="demo-item"><label>Gender</label><span>${Components.esc(patient.gender)}</span></div>
                    <div class="demo-item"><label>Email</label><span>${Components.esc(patient.email)}</span></div>
                    <div class="demo-item"><label>Phone</label><span>${Components.esc(patient.phone)}</span></div>
                    <div class="demo-item"><label>Address</label><span>${Components.esc(patient.address)}</span></div>
                    <div class="demo-item"><label>Insurance</label><span>${Components.esc(patient.insurancePrimary)} (${Components.esc(patient.insuranceId)})</span></div>
                    <div class="demo-item"><label>Mother's Maiden Name</label><span>${Components.esc(patient.mothersMaidenName)}</span></div>
                    <div class="demo-item"><label>Passport Active</label><span>${patient.passportActive ? 'Yes' : 'No'}</span></div>
                </div>
            </div>
        </div>`;
    },

    // ── Visit Notes Tab ──
    renderVisitNotes(patient) {
        const notes = AppState.getPatientNotes(patient.id);
        const query = (AppState.noteSearchQuery || '').toLowerCase();
        let filtered = notes;
        if (query) {
            filtered = notes.filter(n =>
                n.reason.toLowerCase().includes(query) ||
                AppState.getCategoryName(n.category).toLowerCase().includes(query) ||
                n.documentTags.some(t => t.toLowerCase().includes(query)) ||
                n.blocks.some(b => b.content && b.content.toLowerCase().includes(query))
            );
        }

        const noteCards = filtered.map(n => {
            const provider = AppState.getProvider(n.providerId);
            const provName = provider ? provider.fullName : 'Unknown';
            const statusBadge = n.status === 'draft'
                ? Components.statusBadge('Draft', 'warning')
                : Components.statusBadge('Signed', 'success');
            const tags = n.documentTags.map(t => `<span class="doc-tag">${Components.esc(t)}</span>`).join('');
            return `<div class="note-card" data-action="view-note" data-note-id="${n.id}">
                <div class="note-card-header">
                    <div class="note-card-title">
                        <strong>${Components.esc(n.reason || 'Visit Note')}</strong>
                        ${statusBadge}
                    </div>
                    <span class="note-card-date">${Components.formatDate(n.date)}</span>
                </div>
                <div class="note-card-meta">
                    <span>${Components.esc(provName)}</span>
                    <span>${Components.esc(AppState.getCategoryName(n.category))}</span>
                    <span>${Components.esc(AppState.getFormatName(n.format))}</span>
                </div>
                ${tags ? `<div class="note-card-tags">${tags}</div>` : ''}
            </div>`;
        }).join('');

        return `<div class="notes-section">
            ${Components.sectionHeader('Visit Notes', `${filtered.length} notes`, Components.button('+ New Visit Note', 'new-visit-note', 'primary'))}
            <div class="toolbar">
                ${Components.searchInput('note-search', 'Search notes by reason, category, tags, content...', AppState.noteSearchQuery)}
            </div>
            <div class="notes-list">${noteCards}</div>
            ${filtered.length === 0 ? Components.emptyState('No visit notes found.') : ''}
        </div>`;
    },

    // ── Vaccinations Tab ──
    renderVaccinations(patient) {
        const vaccinations = AppState.getPatientVaccinations(patient.id);
        const vaccines = vaccinations.filter(v => !v.isInjectable);
        const injectables = vaccinations.filter(v => v.isInjectable);

        const renderVaxRow = (v) => {
            const statusBadge = v.status === 'declined'
                ? Components.statusBadge('Declined', 'danger')
                : v.recordType === 'Historical'
                    ? Components.statusBadge('Historical', 'info')
                    : Components.statusBadge('Administered', 'success');
            const givenByName = v.givenBy ? (AppState.getProvider(v.givenBy)?.fullName || v.givenBy) : '';
            return `<tr>
                <td><strong>${Components.esc(v.vaccineName)}</strong></td>
                <td>${Components.formatDate(v.givenOn)}</td>
                <td>${Components.esc(v.manufacturer)}</td>
                <td>${Components.esc(v.lotNumber)}</td>
                <td>${Components.esc(v.doseAmount)}${v.doseUnits ? ' ' + Components.esc(v.doseUnits) : ''}${v.seriesNumber ? ' (#' + Components.esc(v.seriesNumber) + ')' : ''}</td>
                <td>${Components.esc(v.site)}</td>
                <td>${Components.esc(givenByName)}</td>
                <td>${statusBadge}</td>
            </tr>`;
        };

        const vaccineTableHtml = vaccines.length > 0
            ? `<div class="table-container"><table class="data-table">
                <thead><tr><th>Vaccine</th><th>Date</th><th>Manufacturer</th><th>Lot #</th><th>Dose</th><th>Site</th><th>Given By</th><th>Status</th></tr></thead>
                <tbody>${vaccines.map(renderVaxRow).join('')}</tbody>
               </table></div>`
            : Components.emptyState('No vaccines recorded.');

        const injectableTableHtml = injectables.length > 0
            ? `<h3 style="margin-top:24px">Injectables (Non-Vaccine)</h3>
               <div class="table-container"><table class="data-table">
                <thead><tr><th>Injectable</th><th>Date</th><th>Manufacturer</th><th>Lot #</th><th>Dose</th><th>Site</th><th>Given By</th><th>Status</th></tr></thead>
                <tbody>${injectables.map(renderVaxRow).join('')}</tbody>
               </table></div>`
            : '';

        return `<div class="vaccinations-section">
            ${Components.sectionHeader('Immunizations & Injectables', `${vaccinations.length} records`, Components.button('+ Add Vaccination', 'add-vaccination', 'primary'))}
            ${vaccineTableHtml}
            ${injectableTableHtml}
        </div>`;
    },

    // ── Vitals Tab ──
    renderVitals(patient) {
        const vitals = AppState.getPatientVitals(patient.id);
        const rows = vitals.map(v => {
            const bp = (v.bloodPressureSystolic && v.bloodPressureDiastolic) ? `${v.bloodPressureSystolic}/${v.bloodPressureDiastolic}` : '';
            return `<tr>
                <td>${Components.formatDate(v.date)}</td>
                <td>${bp}</td>
                <td>${v.heartRate || ''}</td>
                <td>${v.respiratoryRate || ''}</td>
                <td>${v.temperature ? v.temperature + '°' + (v.temperatureUnit || 'F') : ''}</td>
                <td>${v.oxygenSaturation ? v.oxygenSaturation + '%' : ''}</td>
                <td>${v.weight ? v.weight + ' ' + (v.weightUnit || 'lbs') : ''}</td>
                <td>${v.height ? v.height + ' ' + (v.heightUnit || 'in') : ''}</td>
                <td>${v.bmi || ''}</td>
                <td>${v.painLevel !== null && v.painLevel !== undefined ? v.painLevel + '/10' : ''}</td>
            </tr>`;
        }).join('');

        return `<div class="vitals-section">
            ${Components.sectionHeader('Vitals History', `${vitals.length} records`, Components.button('+ Add Historical Vitals', 'add-vitals', 'primary'))}
            ${vitals.length > 0 ? `<div class="table-container"><table class="data-table">
                <thead><tr><th>Date</th><th>BP</th><th>HR</th><th>RR</th><th>Temp</th><th>SpO2</th><th>Weight</th><th>Height</th><th>BMI</th><th>Pain</th></tr></thead>
                <tbody>${rows}</tbody>
            </table></div>` : Components.emptyState('No vitals recorded.')}
        </div>`;
    },

    // ── Care Plans Tab ──
    renderCarePlans(patient) {
        const carePlans = AppState.getPatientCarePlans(patient.id);
        const cpCards = carePlans.map(cp => {
            const provider = AppState.getProvider(cp.providerId);
            const provName = provider ? provider.fullName : 'Unknown';
            const dxList = cp.diagnoses.map(d => `<span class="icd-code">${Components.esc(d)}</span>`).join(' ');
            return `<div class="care-plan-card">
                <div class="cp-header">
                    <span class="cp-date">${Components.formatDate(cp.date)}</span>
                    <span class="cp-provider">${Components.esc(provName)}</span>
                    ${Components.statusBadge(cp.status, cp.status === 'active' ? 'success' : 'default')}
                </div>
                <div class="cp-diagnoses">${dxList}</div>
                <div class="cp-content">${Components.esc(cp.content).replace(/\n/g, '<br>')}</div>
                <div class="cp-actions">
                    <button class="btn btn-xs btn-ghost" data-action="export-careplan" data-cp-id="${cp.id}">Export to Note</button>
                </div>
            </div>`;
        }).join('');

        return `<div class="careplans-section">
            ${Components.sectionHeader('Care Plans', `${carePlans.length} plans`)}
            ${cpCards}
            ${carePlans.length === 0 ? Components.emptyState('No care plans documented. Care plans are created from the Care Plan section of visit notes.') : ''}
        </div>`;
    },

    // ══════════════════════════════════════════════════════
    // TEMPLATES SECTION
    // ══════════════════════════════════════════════════════
    renderTemplates() {
        const templates = AppState.visitNoteTemplates;
        const cards = templates.map(t => {
            const creator = AppState.getProvider(t.createdBy);
            const creatorName = creator ? creator.fullName : 'Unknown';
            const tags = t.documentTags.map(tag => `<span class="doc-tag">${Components.esc(tag)}</span>`).join('');
            const billing = t.billingItems.map(b => `<span class="billing-code">${Components.esc(b.cptCode)}</span>`).join(' ');
            const sections = Object.keys(t.content).map(k => Components.esc(k)).join(', ');
            return `<div class="template-card">
                <div class="template-header">
                    <strong>${Components.esc(t.name)}</strong>
                    <div class="template-actions-menu">
                        <button class="btn btn-xs btn-ghost" data-action="edit-template" data-template-id="${t.id}">Edit</button>
                        <button class="btn btn-xs btn-ghost" data-action="duplicate-template" data-template-id="${t.id}">Duplicate</button>
                        <button class="btn btn-xs btn-danger" data-action="delete-template" data-template-id="${t.id}">Delete</button>
                    </div>
                </div>
                <div class="template-meta">
                    <span>By ${Components.esc(creatorName)}</span>
                    <span>${Components.formatDate(t.createdAt)}</span>
                </div>
                <div class="template-detail"><label>Sections:</label> ${sections || 'None'}</div>
                ${billing ? `<div class="template-detail"><label>Billing:</label> ${billing}</div>` : ''}
                ${t.pos ? `<div class="template-detail"><label>POS:</label> ${Components.esc(t.pos)}</div>` : ''}
                ${tags ? `<div class="template-tags">${tags}</div>` : ''}
            </div>`;
        }).join('');

        return `<div class="content-panel">
            ${Components.sectionHeader('Visit Note Templates', `${templates.length} templates`, Components.button('+ New Template', 'new-template', 'primary'))}
            <div class="template-grid">${cards}</div>
            ${templates.length === 0 ? Components.emptyState('No templates created yet.') : ''}
        </div>`;
    },

    // ══════════════════════════════════════════════════════
    // CATEGORIES SECTION
    // ══════════════════════════════════════════════════════
    renderCategories() {
        const cats = [...AppState.visitNoteCategories].sort((a, b) => a.sortOrder - b.sortOrder);
        const rows = cats.map(c => {
            const defaultStar = c.isDefault ? ' <span class="default-star" title="Default category">&#9733;</span>' : '';
            return `<div class="category-row" data-category-id="${c.id}">
                <div class="category-drag" title="Drag to reorder">&#9776;</div>
                <div class="category-info">
                    <span class="category-name">${Components.esc(c.name)}${defaultStar}</span>
                </div>
                <div class="category-mips">
                    ${Components.toggle('mips-' + c.id, c.countForMIPS, 'Count for MIPS')}
                </div>
                <div class="category-actions">
                    <button class="btn btn-xs btn-ghost" data-action="edit-category" data-category-id="${c.id}">Edit</button>
                    ${!c.isDefault ? `<button class="btn btn-xs btn-danger" data-action="remove-category" data-category-id="${c.id}">Remove</button>` : ''}
                </div>
            </div>`;
        }).join('');

        return `<div class="content-panel">
            ${Components.sectionHeader('Visit Note Categories', `${cats.length} categories`, Components.button('+ Add Category', 'add-category', 'primary'))}
            ${Components.infoBox('info', 'The first category in the list is the default category (marked with a star). Drag to reorder. Admin privileges required for changes.')}
            <div class="categories-list">${rows}</div>
        </div>`;
    },

    // ══════════════════════════════════════════════════════
    // SETTINGS SECTION
    // ══════════════════════════════════════════════════════
    renderSettings() {
        const prefs = AppState.providerPreferences;
        const aptTypes = AppState.appointmentTypes;

        const aptRows = aptTypes.map(a => {
            const fmt = AppState.getFormatName(a.noteFormat);
            const cat = AppState.getCategoryName(a.noteCategory);
            const tmpl = AppState.getTemplateName(a.noteTemplate);
            return `<tr>
                <td><span class="apt-color" style="background:${a.color}"></span>${Components.esc(a.name)}</td>
                <td>${a.duration} min</td>
                <td>${Components.esc(fmt)}</td>
                <td>${Components.esc(cat)}</td>
                <td>${Components.esc(tmpl)}</td>
                <td><button class="btn btn-xs btn-ghost" data-action="edit-appointment-type" data-apt-id="${a.id}">Edit</button></td>
            </tr>`;
        }).join('');

        const formatOptions = VISIT_NOTE_FORMATS.map(f => ({ value: f.id, label: f.name }));

        return `<div class="content-panel">
            ${Components.sectionHeader('Settings')}
            <div class="settings-group">
                <h3>Provider Preferences</h3>
                <div class="setting-row">
                    <div class="setting-info">
                        <label>Coded Visit Note Assessments</label>
                        <p class="setting-desc">Show ICD-10 code search in assessment fields</p>
                    </div>
                    <div class="setting-control">
                        ${Components.toggle('pref-coded-assessments', prefs.codedAssessments, '')}
                    </div>
                </div>
                <div class="setting-row">
                    <div class="setting-info">
                        <label>Show Dx Codes in Print</label>
                        <p class="setting-desc">Display diagnosis codes in printed/faxed/shared notes</p>
                    </div>
                    <div class="setting-control">
                        ${Components.toggle('pref-dx-in-print', prefs.showDxCodesInPrint, '')}
                    </div>
                </div>
                <div class="setting-row">
                    <div class="setting-info">
                        <label>Default Visit Note Format</label>
                        <p class="setting-desc">Format used when creating new visit notes</p>
                    </div>
                    <div class="setting-control">
                        ${Components.dropdown('pref-note-format', prefs.defaultNoteFormat, formatOptions)}
                    </div>
                </div>
            </div>
            <div class="settings-group">
                <h3>Appointment Types & Visit Note Automation</h3>
                <p class="setting-desc">Configure which visit note format, category, and template auto-populate when starting a note from each appointment type.</p>
                <div class="table-container">
                    <table class="data-table">
                        <thead><tr><th>Appointment Type</th><th>Duration</th><th>Note Format</th><th>Category</th><th>Template</th><th>Actions</th></tr></thead>
                        <tbody>${aptRows}</tbody>
                    </table>
                </div>
            </div>
            <div class="settings-group">
                <h3>Practice Information</h3>
                <div class="demographics-grid">
                    <div class="demo-item"><label>Practice Name</label><span>${Components.esc(AppState.currentProvider.practiceName)}</span></div>
                    <div class="demo-item"><label>Address</label><span>${Components.esc(AppState.currentProvider.practiceAddress)}</span></div>
                    <div class="demo-item"><label>Phone</label><span>${Components.esc(AppState.currentProvider.practicePhone)}</span></div>
                    <div class="demo-item"><label>Fax</label><span>${Components.esc(AppState.currentProvider.practiceFax)}</span></div>
                </div>
            </div>
        </div>`;
    },

    // ══════════════════════════════════════════════════════
    // MODALS
    // ══════════════════════════════════════════════════════
    renderModal() {
        if (!AppState.activeModal) return '';

        switch (AppState.activeModal) {
            case 'add-problem': return this.renderAddProblemModal();
            case 'edit-problem': return this.renderEditProblemModal();
            case 'add-vaccination': return this.renderAddVaccinationModal();
            case 'add-vitals': return this.renderAddVitalsModal();
            case 'new-visit-note': return this.renderNewVisitNoteModal();
            case 'view-note': return this.renderViewNoteModal();
            case 'add-block': return this.renderAddBlockModal();
            case 'add-billing': return this.renderAddBillingModal();
            case 'new-template': return this.renderNewTemplateModal();
            case 'edit-template': return this.renderEditTemplateModal();
            case 'add-category': return this.renderAddCategoryModal();
            case 'edit-category': return this.renderEditCategoryModal();
            case 'add-tag': return this.renderAddTagModal();
            case 'edit-appointment-type': return this.renderEditAppointmentTypeModal();
            case 'confirm-delete': return this.renderConfirmDeleteModal();
            default: return '';
        }
    },

    renderAddProblemModal() {
        const body = `
            <div class="form-group">
                <label>Search Diagnosis</label>
                <input type="text" class="form-input" id="problem-search" placeholder="Search by name, ICD-10 code, or abbreviation..." data-input="problem-search">
                <div class="search-results" id="problem-search-results"></div>
            </div>
            <div class="form-group">
                <label>Title <span class="required">*</span></label>
                <input type="text" class="form-input" id="problem-title" placeholder="Problem title">
            </div>
            <div class="form-group">
                <label>ICD-10 Code</label>
                <input type="text" class="form-input" id="problem-icd10" placeholder="e.g. E11.65">
            </div>
            <div class="form-group">
                <label>Onset Date</label>
                <input type="text" class="form-input" id="problem-dx-date" placeholder="YYYY-MM-DD" value="${new Date().toISOString().split('T')[0]}">
            </div>
            <div class="form-group">
                <label>Status</label>
                ${Components.dropdown('problem-status', 'Active', ['Active', 'Controlled', 'Resolved'])}
            </div>
            <div class="form-group">
                <label>Synopsis</label>
                <textarea class="form-textarea" id="problem-synopsis" rows="3" placeholder="Clinical notes..."></textarea>
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save & Add Another', 'save-problem-and-add', 'secondary')}
            ${Components.button('Save', 'save-problem', 'primary')}`;
        return Components.modal('add-problem', 'Add Problem', body, footer);
    },

    renderEditProblemModal() {
        const prob = AppState.modalData;
        if (!prob) return '';
        const body = `
            <div class="form-group">
                <label>Title <span class="required">*</span></label>
                <input type="text" class="form-input" id="problem-title" value="${Components.escAttr(prob.title)}">
            </div>
            <div class="form-group">
                <label>ICD-10 Code</label>
                <input type="text" class="form-input" id="problem-icd10" value="${Components.escAttr(prob.icd10)}">
            </div>
            <div class="form-group">
                <label>Onset Date</label>
                <input type="text" class="form-input" id="problem-dx-date" value="${Components.escAttr(prob.dxDate)}">
            </div>
            <div class="form-group">
                <label>Status</label>
                ${Components.dropdown('problem-status', prob.status, ['Active', 'Controlled', 'Resolved'])}
            </div>
            <div class="form-group">
                <label>Synopsis</label>
                <textarea class="form-textarea" id="problem-synopsis" rows="3">${Components.esc(prob.synopsis)}</textarea>
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save Changes', 'save-edit-problem', 'primary')}`;
        return Components.modal('edit-problem', 'Edit Problem', body, footer);
    },

    renderAddVaccinationModal() {
        const data = AppState.modalData || {};
        const recordTypeOptions = ['New', 'Historical', 'Declined'];
        const body = `
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Record Type</label>
                    ${Components.dropdown('vax-record-type', data.recordType || 'New', recordTypeOptions)}
                </div>
            </div>
            <div class="form-group">
                <label>Vaccine Name <span class="required">*</span></label>
                <input type="text" class="form-input" id="vax-name" placeholder="Type to search or enter vaccine name..." value="${Components.escAttr(data.vaccineName || '')}">
                <div class="search-results" id="vax-name-results"></div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Manufacturer</label>
                    ${Components.dropdown('vax-manufacturer', data.manufacturer || '', VACCINE_MANUFACTURERS.map(m => ({value: m, label: m})))}
                </div>
                <div class="form-group flex-1">
                    <label>Lot #</label>
                    <input type="text" class="form-input" id="vax-lot" value="${Components.escAttr(data.lotNumber || '')}">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>NDC #</label>
                    <input type="text" class="form-input" id="vax-ndc" value="${Components.escAttr(data.ndc || '')}">
                </div>
                <div class="form-group flex-1">
                    <label>Expiration</label>
                    <input type="text" class="form-input" id="vax-expiration" placeholder="YYYY-MM-DD" value="${Components.escAttr(data.expirationDate || '')}">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Dose Amount</label>
                    <input type="text" class="form-input" id="vax-dose-amount" value="${Components.escAttr(data.doseAmount || '')}">
                </div>
                <div class="form-group flex-1">
                    <label>Units</label>
                    ${Components.dropdown('vax-dose-units', data.doseUnits || 'mL', ['mL', 'mg', 'mcg', 'units'])}
                </div>
                <div class="form-group flex-1">
                    <label>Series #</label>
                    <input type="text" class="form-input" id="vax-series" value="${Components.escAttr(data.seriesNumber || '')}">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Method</label>
                    ${Components.dropdown('vax-method', data.method || '', ADMIN_METHODS)}
                </div>
                <div class="form-group flex-1">
                    <label>Site</label>
                    ${Components.dropdown('vax-site', data.site || '', ADMIN_SITES)}
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Given On</label>
                    <input type="text" class="form-input" id="vax-given-on" placeholder="YYYY-MM-DD" value="${Components.escAttr(data.givenOn || new Date().toISOString().split('T')[0])}">
                </div>
                <div class="form-group flex-1">
                    <label>VIS Date</label>
                    <input type="text" class="form-input" id="vax-vis-date" placeholder="YYYY-MM-DD" value="${Components.escAttr(data.visDate || '')}">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Ordered By</label>
                    ${Components.dropdown('vax-ordered-by', data.orderedBy || AppState.currentProvider.id, AppState.providers.map(p => ({value: p.id, label: p.fullName})))}
                </div>
                <div class="form-group flex-1">
                    <label>Given By</label>
                    <input type="text" class="form-input" id="vax-given-by" value="${Components.escAttr(data.givenBy || AppState.currentProvider.fullName)}">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Recall</label>
                    ${Components.dropdown('vax-recall', data.recall || '', RECALL_OPTIONS)}
                </div>
                <div class="form-group flex-1">
                    <label>Program</label>
                    ${Components.dropdown('vax-program', data.program || 'Not VFC Eligible', PROGRAM_OPTIONS)}
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Funded By</label>
                    ${Components.dropdown('vax-funded-by', data.fundedBy || 'Private', FUNDED_BY_OPTIONS)}
                </div>
            </div>
            <div class="form-group">
                <label>Reason</label>
                <input type="text" class="form-input" id="vax-reason" value="${Components.escAttr(data.reason || '')}">
            </div>
            <div class="form-group">
                <label>Notes</label>
                <textarea class="form-textarea" id="vax-notes" rows="2">${Components.esc(data.notes || '')}</textarea>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    ${Components.toggle('vax-is-injectable', data.isInjectable || false, 'Is Injectable')}
                </div>
                <div class="form-group flex-1">
                    ${Components.toggle('vax-not-send-registry', data.notSendToRegistry || false, 'Do Not Send to Registry')}
                </div>
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save & Add Another', 'save-vaccination-and-add', 'secondary')}
            ${Components.button('Save', 'save-vaccination', 'primary')}`;
        return Components.modal('add-vaccination', 'Add Vaccination / Injectable', body, footer, 'lg');
    },

    renderAddVitalsModal() {
        const body = `
            <div class="form-group">
                <label>Date</label>
                <input type="text" class="form-input" id="vitals-date" placeholder="YYYY-MM-DD" value="${new Date().toISOString().split('T')[0]}">
            </div>
            ${Components.infoBox('info', 'Update the date when entering historical vitals (e.g., home blood pressure readings).')}
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Systolic BP</label>
                    <input type="text" class="form-input" id="vitals-sys" placeholder="mmHg">
                </div>
                <div class="form-group flex-1">
                    <label>Diastolic BP</label>
                    <input type="text" class="form-input" id="vitals-dia" placeholder="mmHg">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Heart Rate</label>
                    <input type="text" class="form-input" id="vitals-hr" placeholder="bpm">
                </div>
                <div class="form-group flex-1">
                    <label>Respiratory Rate</label>
                    <input type="text" class="form-input" id="vitals-rr" placeholder="breaths/min">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Temperature</label>
                    <input type="text" class="form-input" id="vitals-temp" placeholder="degrees">
                </div>
                <div class="form-group flex-1">
                    <label>Temp Unit</label>
                    ${Components.dropdown('vitals-temp-unit', 'F', ['F', 'C'])}
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>O2 Saturation</label>
                    <input type="text" class="form-input" id="vitals-spo2" placeholder="%">
                </div>
                <div class="form-group flex-1">
                    <label>Pain Level (0-10)</label>
                    <input type="text" class="form-input" id="vitals-pain" placeholder="0-10">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Weight</label>
                    <input type="text" class="form-input" id="vitals-weight" placeholder="">
                </div>
                <div class="form-group flex-1">
                    <label>Weight Unit</label>
                    ${Components.dropdown('vitals-weight-unit', 'lbs', ['lbs', 'kg'])}
                </div>
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Height</label>
                    <input type="text" class="form-input" id="vitals-height" placeholder="">
                </div>
                <div class="form-group flex-1">
                    <label>Height Unit</label>
                    ${Components.dropdown('vitals-height-unit', 'in', ['in', 'cm'])}
                </div>
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save & Add Another', 'save-vitals-and-add', 'secondary')}
            ${Components.button('Save', 'save-vitals', 'primary')}`;
        return Components.modal('add-vitals', 'Add Historical Vitals', body, footer);
    },

    renderNewVisitNoteModal() {
        const catOptions = AppState.visitNoteCategories.map(c => ({ value: c.id, label: c.name }));
        const fmtOptions = VISIT_NOTE_FORMATS.map(f => ({ value: f.id, label: f.name }));
        const tmplOptions = [{ value: '', label: 'None' }, ...AppState.visitNoteTemplates.map(t => ({ value: t.id, label: t.name }))];

        const body = `
            <div class="form-group">
                <label>Reason for Visit</label>
                <input type="text" class="form-input" id="note-reason" placeholder="e.g. Follow-up: Diabetes Management">
            </div>
            <div class="form-row">
                <div class="form-group flex-1">
                    <label>Visit Note Format</label>
                    ${Components.dropdown('note-format', AppState.providerPreferences.defaultNoteFormat, fmtOptions)}
                </div>
                <div class="form-group flex-1">
                    <label>Category</label>
                    ${Components.dropdown('note-category', AppState.visitNoteCategories.find(c => c.isDefault)?.id || 'cat_001', catOptions)}
                </div>
            </div>
            <div class="form-group">
                <label>Template</label>
                ${Components.dropdown('note-template', '', tmplOptions)}
            </div>
            <div class="form-group">
                <label>Date</label>
                <input type="text" class="form-input" id="note-date" value="${new Date().toISOString().split('T')[0]}">
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Create Note', 'create-visit-note', 'primary')}`;
        return Components.modal('new-visit-note', 'New Visit Note', body, footer);
    },

    renderViewNoteModal() {
        const note = AppState.modalData;
        if (!note) return '';
        const provider = AppState.getProvider(note.providerId);
        const provName = provider ? provider.fullName : 'Unknown';
        const isDraft = note.status === 'draft';

        const blocksHtml = note.blocks.map((block, idx) => {
            const blockName = STANDARD_BLOCKS.find(b => b.type === block.type)?.name || block.type;
            const content = isDraft
                ? `<textarea class="form-textarea block-content" data-block-idx="${idx}" rows="4">${Components.esc(block.content)}</textarea>`
                : `<div class="block-content-display">${Components.esc(block.content).replace(/\n/g, '<br>')}</div>`;
            return `<div class="note-block">
                <div class="block-header">
                    <h4>${Components.esc(blockName)}</h4>
                    ${isDraft ? `<button class="btn btn-xs btn-danger" data-action="remove-block" data-note-id="${note.id}" data-block-idx="${idx}">Remove</button>` : ''}
                </div>
                ${content}
            </div>`;
        }).join('');

        const billingHtml = note.billingItems.length > 0
            ? `<div class="billing-section"><h4>Billing</h4>${note.billingItems.map((b, i) =>
                `<div class="billing-item"><span class="billing-code">${Components.esc(b.cptCode)}</span> ${Components.esc(b.description)} ${isDraft ? `<button class="btn btn-xs btn-danger" data-action="remove-billing" data-note-id="${note.id}" data-billing-idx="${i}">&times;</button>` : ''}</div>`
            ).join('')}</div>` : '';

        const tagsHtml = note.documentTags.length > 0
            ? `<div class="note-tags">${note.documentTags.map(t => `<span class="doc-tag">${Components.esc(t)}</span>`).join('')}</div>` : '';

        const body = `
            <div class="note-view-header">
                <div class="note-view-meta">
                    <span><strong>Provider:</strong> ${Components.esc(provName)}</span>
                    <span><strong>Date:</strong> ${Components.formatDateTime(note.date)}</span>
                    <span><strong>Format:</strong> ${Components.esc(AppState.getFormatName(note.format))}</span>
                    <span><strong>Category:</strong> ${Components.esc(AppState.getCategoryName(note.category))}</span>
                    <span><strong>Status:</strong> ${note.status === 'draft' ? Components.statusBadge('Draft', 'warning') : Components.statusBadge('Signed ' + Components.formatDateTime(note.signedAt), 'success')}</span>
                </div>
                ${note.reason ? `<div class="note-view-reason"><strong>Reason:</strong> ${Components.esc(note.reason)}</div>` : ''}
                ${tagsHtml}
            </div>
            <div class="note-blocks">${blocksHtml}</div>
            ${billingHtml}
            ${isDraft ? `<div class="add-block-bar">
                ${Components.button('+ Add Block', 'show-add-block', 'ghost')}
                ${Components.button('+ Add Billing Item', 'show-add-billing', 'ghost')}
            </div>` : ''}`;
        const footer = isDraft
            ? `${Components.button('Close', 'close-modal', 'ghost')} ${Components.button('Save Draft', 'save-note-draft', 'secondary')} ${Components.button('Sign Note', 'sign-visit-note', 'primary')}`
            : `${Components.button('Close', 'close-modal', 'ghost')}`;
        return Components.modal('view-note', note.reason || 'Visit Note', body, footer, 'lg');
    },

    renderAddBlockModal() {
        const noteId = AppState.modalData?.noteId;
        const note = AppState.visitNotes.find(n => n.id === noteId);
        const existingTypes = note ? note.blocks.map(b => b.type) : [];
        const available = STANDARD_BLOCKS.filter(b => b.canAddMultiple || !existingTypes.includes(b.type));
        const blockItems = available.map(b =>
            `<div class="block-option" data-action="add-block-to-note" data-note-id="${noteId}" data-block-type="${b.type}">
                ${Components.esc(b.name)}
            </div>`
        ).join('');
        const body = `<div class="block-options-list">${blockItems}</div>`;
        const footer = Components.button('Cancel', 'close-modal', 'ghost');
        return Components.modal('add-block', 'Add Block to Note', body, footer);
    },

    renderAddBillingModal() {
        const noteId = AppState.modalData?.noteId;
        const body = `
            <div class="form-group">
                <label>CPT Code <span class="required">*</span></label>
                <input type="text" class="form-input" id="billing-cpt" placeholder="e.g. 99213">
            </div>
            <div class="form-group">
                <label>Description <span class="required">*</span></label>
                <input type="text" class="form-input" id="billing-description" placeholder="e.g. Office visit, established, low complexity">
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Add Billing Item', 'save-billing-item', 'primary')}`;
        return Components.modal('add-billing', 'Add Billing Item', body, footer);
    },

    renderNewTemplateModal() {
        const body = `
            <div class="form-group">
                <label>Template Name <span class="required">*</span></label>
                <input type="text" class="form-input" id="template-name" placeholder="e.g. Annual Wellness Visit">
            </div>
            <div class="form-group">
                <label>HPI Content</label>
                <textarea class="form-textarea" id="template-hpi" rows="3" placeholder="History of Present Illness template text..."></textarea>
            </div>
            <div class="form-group">
                <label>ROS Content</label>
                <textarea class="form-textarea" id="template-ros" rows="3" placeholder="Review of Systems template text..."></textarea>
            </div>
            <div class="form-group">
                <label>PE Content</label>
                <textarea class="form-textarea" id="template-pe" rows="3" placeholder="Physical Exam template text..."></textarea>
            </div>
            <div class="form-group">
                <label>Assessment Content</label>
                <textarea class="form-textarea" id="template-assessment" rows="2" placeholder="Assessment template text..."></textarea>
            </div>
            <div class="form-group">
                <label>CPT Code</label>
                <input type="text" class="form-input" id="template-cpt" placeholder="e.g. 99213">
            </div>
            <div class="form-group">
                <label>CPT Description</label>
                <input type="text" class="form-input" id="template-cpt-desc" placeholder="e.g. Office visit, established">
            </div>
            <div class="form-group">
                <label>Place of Service (POS)</label>
                <input type="text" class="form-input" id="template-pos" placeholder="e.g. 02 for Telehealth">
            </div>
            <div class="form-group">
                <label>Billing Notes</label>
                <input type="text" class="form-input" id="template-billing-notes" placeholder="">
            </div>
            <div class="form-group">
                <label>Document Tags (comma-separated)</label>
                <input type="text" class="form-input" id="template-tags" placeholder="e.g. Annual, Preventive">
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save Template', 'save-template', 'primary')}`;
        return Components.modal('new-template', 'New Visit Note Template', body, footer, 'lg');
    },

    renderEditTemplateModal() {
        const tmpl = AppState.modalData;
        if (!tmpl) return '';
        const body = `
            <div class="form-group">
                <label>Template Name <span class="required">*</span></label>
                <input type="text" class="form-input" id="template-name" value="${Components.escAttr(tmpl.name)}">
            </div>
            <div class="form-group">
                <label>HPI Content</label>
                <textarea class="form-textarea" id="template-hpi" rows="3">${Components.esc(tmpl.content.hpi || '')}</textarea>
            </div>
            <div class="form-group">
                <label>ROS Content</label>
                <textarea class="form-textarea" id="template-ros" rows="3">${Components.esc(tmpl.content.ros || '')}</textarea>
            </div>
            <div class="form-group">
                <label>PE Content</label>
                <textarea class="form-textarea" id="template-pe" rows="3">${Components.esc(tmpl.content.pe || '')}</textarea>
            </div>
            <div class="form-group">
                <label>Assessment Content</label>
                <textarea class="form-textarea" id="template-assessment" rows="2">${Components.esc(tmpl.content.assessment || '')}</textarea>
            </div>
            <div class="form-group">
                <label>CPT Code</label>
                <input type="text" class="form-input" id="template-cpt" value="${Components.escAttr(tmpl.billingItems[0]?.cptCode || '')}">
            </div>
            <div class="form-group">
                <label>CPT Description</label>
                <input type="text" class="form-input" id="template-cpt-desc" value="${Components.escAttr(tmpl.billingItems[0]?.description || '')}">
            </div>
            <div class="form-group">
                <label>Place of Service (POS)</label>
                <input type="text" class="form-input" id="template-pos" value="${Components.escAttr(tmpl.pos || '')}">
            </div>
            <div class="form-group">
                <label>Billing Notes</label>
                <input type="text" class="form-input" id="template-billing-notes" value="${Components.escAttr(tmpl.billingNotes || '')}">
            </div>
            <div class="form-group">
                <label>Document Tags (comma-separated)</label>
                <input type="text" class="form-input" id="template-tags" value="${Components.escAttr(tmpl.documentTags.join(', '))}">
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save Changes', 'save-edit-template', 'primary')}`;
        return Components.modal('edit-template', 'Edit Template', body, footer, 'lg');
    },

    renderAddCategoryModal() {
        const body = `
            <div class="form-group">
                <label>Category Name <span class="required">*</span></label>
                <input type="text" class="form-input" id="category-name" placeholder="e.g. Urgent Visit">
            </div>
            <div class="form-group">
                ${Components.toggle('category-mips', false, 'Count for MIPS?')}
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save', 'save-category', 'primary')}`;
        return Components.modal('add-category', 'Add Visit Note Category', body, footer);
    },

    renderEditCategoryModal() {
        const cat = AppState.modalData;
        if (!cat) return '';
        const body = `
            <div class="form-group">
                <label>Category Name <span class="required">*</span></label>
                <input type="text" class="form-input" id="category-name" value="${Components.escAttr(cat.name)}">
            </div>
            <div class="form-group">
                ${Components.toggle('category-mips', cat.countForMIPS, 'Count for MIPS?')}
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save Changes', 'save-edit-category', 'primary')}`;
        return Components.modal('edit-category', 'Edit Category', body, footer);
    },

    renderAddTagModal() {
        const body = `
            <div class="form-group">
                <label>Tag Name</label>
                <input type="text" class="form-input" id="tag-name" placeholder="e.g. *COVID-Booster-Due or Diabetes-Management">
                ${Components.infoBox('info', 'Prefix with * to pin the tag at the top of the alphabetical list.')}
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Add Tag', 'save-tag', 'primary')}`;
        return Components.modal('add-tag', 'Add Patient Tag', body, footer);
    },

    renderEditAppointmentTypeModal() {
        const apt = AppState.modalData;
        if (!apt) return '';
        const catOptions = AppState.visitNoteCategories.map(c => ({ value: c.id, label: c.name }));
        const fmtOptions = VISIT_NOTE_FORMATS.map(f => ({ value: f.id, label: f.name }));
        const tmplOptions = [{ value: '', label: 'None' }, ...AppState.visitNoteTemplates.map(t => ({ value: t.id, label: t.name }))];
        const body = `
            <div class="form-group">
                <label>Appointment Type: <strong>${Components.esc(apt.name)}</strong></label>
            </div>
            <div class="form-group">
                <label>Visit Note Format</label>
                ${Components.dropdown('apt-note-format', apt.noteFormat, fmtOptions)}
            </div>
            <div class="form-group">
                <label>Visit Note Category</label>
                ${Components.dropdown('apt-note-category', apt.noteCategory, catOptions)}
            </div>
            <div class="form-group">
                <label>Visit Note Template</label>
                ${Components.dropdown('apt-note-template', apt.noteTemplate, tmplOptions)}
            </div>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Save', 'save-appointment-type', 'primary')}`;
        return Components.modal('edit-appointment-type', 'Edit Appointment Type', body, footer);
    },

    renderConfirmDeleteModal() {
        const data = AppState.modalData || {};
        const body = `<p>${Components.esc(data.message || 'Are you sure you want to delete this item?')}</p>`;
        const footer = `
            ${Components.button('Cancel', 'close-modal', 'ghost')}
            ${Components.button('Delete', 'confirm-delete', 'danger')}`;
        return Components.modal('confirm-delete', data.title || 'Confirm Delete', body, footer);
    },

    // ── Toast ──
    renderToast() {
        if (!AppState.toastMessage) return '';
        return `<div class="toast">${Components.esc(AppState.toastMessage)}</div>`;
    }
};
