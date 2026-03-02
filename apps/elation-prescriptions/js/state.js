const AppState = {
    // Persistent data
    currentUser: null,
    currentPatient: null,
    permanentRxMeds: [],
    permanentOtcMeds: [],
    temporaryMeds: [],
    discontinuedMeds: [],
    canceledScripts: [],
    pharmacies: [],
    refillRequests: [],
    changeRequests: [],
    rxTemplates: [],
    customSigs: [],
    medicationDatabase: [],
    drugInteractions: [],
    formularyData: {},
    settings: {},
    providers: [],
    diagnosisCodes: [],

    // ID counters
    _nextPrxId: 100,
    _nextOtcId: 100,
    _nextTmpId: 100,
    _nextDiscId: 100,
    _nextCxlId: 100,
    _nextRrId: 100,
    _nextCrId: 100,
    _nextTplId: 100,
    _nextSigId: 100,
    _nextAlgId: 100,

    // UI state (not persisted)
    currentView: 'chart',
    currentSubView: null,
    selectedMedId: null,
    prescribeFormOpen: false,
    prescribeFormData: null,
    documentMedFormOpen: false,
    discontinueModalOpen: false,
    discontinueTarget: null,
    reconcileOpen: false,
    bulkRefillOpen: false,
    settingsTab: 'templates',
    searchQuery: '',
    medHistorySearch: '',
    medHistoryFilter: 'all',
    activeDropdown: null,
    toasts: [],
    confirmModal: null,
    pharmacySearchQuery: '',
    selectedRefillIds: new Set(),

    _listeners: [],

    subscribe(fn) {
        this._listeners.push(fn);
    },

    notify() {
        this._persist();
        this._pushStateToServer();
        for (const fn of this._listeners) {
            fn();
        }
    },

    init() {
        const persisted = this._loadPersistedData();
        if (persisted) {
            this.currentUser = persisted.currentUser || {};
            this.currentPatient = persisted.currentPatient || {};
            this.permanentRxMeds = persisted.permanentRxMeds || [];
            this.permanentOtcMeds = persisted.permanentOtcMeds || [];
            this.temporaryMeds = persisted.temporaryMeds || [];
            this.discontinuedMeds = persisted.discontinuedMeds || [];
            this.canceledScripts = persisted.canceledScripts || [];
            this.pharmacies = persisted.pharmacies || [];
            this.refillRequests = persisted.refillRequests || [];
            this.changeRequests = persisted.changeRequests || [];
            this.rxTemplates = persisted.rxTemplates || [];
            this.customSigs = persisted.customSigs || [];
            this.medicationDatabase = persisted.medicationDatabase || [];
            this.drugInteractions = persisted.drugInteractions || [];
            this.formularyData = persisted.formularyData || {};
            this.settings = persisted.settings || {};
            this.providers = persisted.providers || [];
            this.diagnosisCodes = persisted.diagnosisCodes || [];
            this._nextPrxId = persisted._nextPrxId || 100;
            this._nextOtcId = persisted._nextOtcId || 100;
            this._nextTmpId = persisted._nextTmpId || 100;
            this._nextDiscId = persisted._nextDiscId || 100;
            this._nextCxlId = persisted._nextCxlId || 100;
            this._nextRrId = persisted._nextRrId || 100;
            this._nextCrId = persisted._nextCrId || 100;
            this._nextTplId = persisted._nextTplId || 100;
            this._nextSigId = persisted._nextSigId || 100;
            this._nextAlgId = persisted._nextAlgId || 100;
        } else {
            this._loadSeedData();
        }
        this.notify();
    },

    _loadSeedData() {
        this.currentUser = JSON.parse(JSON.stringify(CURRENT_USER));
        this.currentPatient = JSON.parse(JSON.stringify(CURRENT_PATIENT));
        this.permanentRxMeds = JSON.parse(JSON.stringify(PERMANENT_RX_MEDS));
        this.permanentOtcMeds = JSON.parse(JSON.stringify(PERMANENT_OTC_MEDS));
        this.temporaryMeds = JSON.parse(JSON.stringify(TEMPORARY_MEDS));
        this.discontinuedMeds = JSON.parse(JSON.stringify(DISCONTINUED_MEDS));
        this.canceledScripts = JSON.parse(JSON.stringify(CANCELED_SCRIPTS));
        this.pharmacies = JSON.parse(JSON.stringify(PHARMACIES));
        this.refillRequests = JSON.parse(JSON.stringify(REFILL_REQUESTS));
        this.changeRequests = JSON.parse(JSON.stringify(CHANGE_REQUESTS));
        this.rxTemplates = JSON.parse(JSON.stringify(RX_TEMPLATES));
        this.customSigs = JSON.parse(JSON.stringify(CUSTOM_SIGS));
        this.medicationDatabase = JSON.parse(JSON.stringify(MEDICATION_DATABASE));
        this.drugInteractions = JSON.parse(JSON.stringify(DRUG_INTERACTIONS));
        this.formularyData = JSON.parse(JSON.stringify(FORMULARY_DATA));
        this.settings = JSON.parse(JSON.stringify(SETTINGS));
        this.providers = JSON.parse(JSON.stringify(PROVIDERS));
        this.diagnosisCodes = JSON.parse(JSON.stringify(DIAGNOSIS_CODES));
        this._nextPrxId = 100;
        this._nextOtcId = 100;
        this._nextTmpId = 100;
        this._nextDiscId = 100;
        this._nextCxlId = 100;
        this._nextRrId = 100;
        this._nextCrId = 100;
        this._nextTplId = 100;
        this._nextSigId = 100;
        this._nextAlgId = 100;
    },

    _loadPersistedData() {
        try {
            const saved = localStorage.getItem('elationPrescriptionsState');
            if (!saved) return null;
            const parsed = JSON.parse(saved);
            if (parsed._seedVersion !== SEED_DATA_VERSION) {
                localStorage.removeItem('elationPrescriptionsState');
                return null;
            }
            return parsed;
        } catch (e) {
            return null;
        }
    },

    _persist() {
        const state = this.getSerializableState();
        localStorage.setItem('elationPrescriptionsState', JSON.stringify(state));
    },

    _pushStateToServer() {
        const state = this.getSerializableState();
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(state)
        }).catch(() => {});
    },

    getSerializableState() {
        return {
            _seedVersion: SEED_DATA_VERSION,
            currentUser: this.currentUser,
            currentPatient: this.currentPatient,
            permanentRxMeds: this.permanentRxMeds,
            permanentOtcMeds: this.permanentOtcMeds,
            temporaryMeds: this.temporaryMeds,
            discontinuedMeds: this.discontinuedMeds,
            canceledScripts: this.canceledScripts,
            pharmacies: this.pharmacies,
            refillRequests: this.refillRequests,
            changeRequests: this.changeRequests,
            rxTemplates: this.rxTemplates,
            customSigs: this.customSigs,
            medicationDatabase: this.medicationDatabase,
            drugInteractions: this.drugInteractions,
            formularyData: this.formularyData,
            settings: this.settings,
            providers: this.providers,
            diagnosisCodes: this.diagnosisCodes,
            _nextPrxId: this._nextPrxId,
            _nextOtcId: this._nextOtcId,
            _nextTmpId: this._nextTmpId,
            _nextDiscId: this._nextDiscId,
            _nextCxlId: this._nextCxlId,
            _nextRrId: this._nextRrId,
            _nextCrId: this._nextCrId,
            _nextTplId: this._nextTplId,
            _nextSigId: this._nextSigId,
            _nextAlgId: this._nextAlgId
        };
    },

    resetToSeedData() {
        localStorage.removeItem('elationPrescriptionsState');
        this._loadSeedData();
        this.currentView = 'chart';
        this.currentSubView = null;
        this.selectedMedId = null;
        this.prescribeFormOpen = false;
        this.prescribeFormData = null;
        this.documentMedFormOpen = false;
        this.discontinueModalOpen = false;
        this.discontinueTarget = null;
        this.reconcileOpen = false;
        this.bulkRefillOpen = false;
        this.settingsTab = 'templates';
        this.searchQuery = '';
        this.medHistorySearch = '';
        this.medHistoryFilter = 'all';
        this.activeDropdown = null;
        this.toasts = [];
        this.confirmModal = null;
        this.pharmacySearchQuery = '';
        this.selectedRefillIds = new Set();
        this.notify();
    },

    // --- Query methods ---

    getAllActiveMeds() {
        return [...this.permanentRxMeds, ...this.permanentOtcMeds, ...this.temporaryMeds];
    },

    getAllMeds() {
        return [...this.permanentRxMeds, ...this.permanentOtcMeds, ...this.temporaryMeds, ...this.discontinuedMeds, ...this.canceledScripts];
    },

    getMedById(id) {
        return this.getAllMeds().find(m => m.id === id) || null;
    },

    getPharmacyById(id) {
        return this.pharmacies.find(p => p.id === id) || null;
    },

    getPendingRefillRequests() {
        return this.refillRequests.filter(r => r.status === 'pending');
    },

    getPendingChangeRequests() {
        return this.changeRequests.filter(r => r.status === 'pending');
    },

    getAllPendingRequests() {
        return [...this.getPendingRefillRequests(), ...this.getPendingChangeRequests()];
    },

    searchMedications(query) {
        if (!query || query.length < 2) return [];
        const q = query.toLowerCase();
        const results = [];
        // Search templates first
        for (const tpl of this.rxTemplates) {
            if (tpl.medicationName.toLowerCase().includes(q)) {
                results.push({ ...tpl, isTemplate: true });
            }
        }
        // Search database
        for (const med of this.medicationDatabase) {
            if (med.name.toLowerCase().includes(q) || (med.drugClass && med.drugClass.toLowerCase().includes(q))) {
                for (const strength of med.strengths) {
                    results.push({
                        id: `${med.id}_${strength}`,
                        medicationName: `${med.name} ${strength} ${med.form}`,
                        name: med.name,
                        strength: strength,
                        form: med.form,
                        type: med.type,
                        drugClass: med.drugClass,
                        generic: med.generic,
                        controlled: med.controlled || false,
                        schedule: med.schedule || null,
                        isTemplate: false
                    });
                }
            }
        }
        return results.slice(0, 30);
    },

    searchPharmacies(query) {
        if (!query || query.length < 2) return this.pharmacies;
        const q = query.toLowerCase();
        return this.pharmacies.filter(p =>
            p.name.toLowerCase().includes(q) ||
            p.city.toLowerCase().includes(q) ||
            p.zip.includes(q) ||
            p.phone.includes(q) ||
            (p.storeNumber && p.storeNumber.includes(q))
        );
    },

    getInteractionsForMed(medName) {
        if (!medName) return [];
        const baseName = medName.split(' ')[0].toLowerCase();
        const level = this.settings.drugDecisionSupport.drugToDrugLevel;
        return this.drugInteractions.filter(di => {
            const d1 = di.drug1.toLowerCase();
            const d2 = di.drug2.toLowerCase();
            const matches = d1.includes(baseName) || d2.includes(baseName);
            if (!matches) return false;
            if (level === 'major_only') return di.severity === 'major';
            if (level === 'major_moderate') return di.severity === 'major' || di.severity === 'moderate';
            return true;
        });
    },

    getAllergyAlertsForMed(medName) {
        if (!medName || !this.settings.drugDecisionSupport.drugToAllergyEnabled) return [];
        const baseName = medName.toLowerCase();
        const alerts = [];
        for (const allergy of this.currentPatient.allergies) {
            if (allergy.type !== 'drug') continue;
            const allergen = allergy.allergen.toLowerCase();
            if (baseName.includes('amoxicillin') && allergen === 'penicillin') {
                alerts.push({ allergen: allergy.allergen, reaction: allergy.reaction, severity: allergy.severity, medication: medName });
            }
            if (baseName.includes('ampicillin') && allergen === 'penicillin') {
                alerts.push({ allergen: allergy.allergen, reaction: allergy.reaction, severity: allergy.severity, medication: medName });
            }
            if (baseName.includes('sulfamethoxazole') && allergen === 'sulfonamides') {
                alerts.push({ allergen: allergy.allergen, reaction: allergy.reaction, severity: allergy.severity, medication: medName });
            }
            if (baseName.includes('codeine') && allergen === 'codeine') {
                alerts.push({ allergen: allergy.allergen, reaction: allergy.reaction, severity: allergy.severity, medication: medName });
            }
        }
        return alerts;
    },

    getFormularyInfo(medName) {
        return this.formularyData[medName] || null;
    },

    getMedHistoryFiltered() {
        let meds = [];
        switch (this.medHistoryFilter) {
            case 'permanent_rx': meds = [...this.permanentRxMeds]; break;
            case 'permanent_otc': meds = [...this.permanentOtcMeds]; break;
            case 'temporary': meds = [...this.temporaryMeds]; break;
            case 'discontinued': meds = [...this.discontinuedMeds]; break;
            case 'canceled': meds = [...this.canceledScripts]; break;
            default: meds = this.getAllMeds();
        }
        if (this.medHistorySearch) {
            const q = this.medHistorySearch.toLowerCase();
            meds = meds.filter(m => m.medicationName.toLowerCase().includes(q));
        }
        return meds.sort((a, b) => a.medicationName.localeCompare(b.medicationName));
    },

    // --- Mutation methods ---

    addPrescription(formData) {
        const id = `prx_${String(this._nextPrxId++).padStart(3, '0')}`;
        const now = new Date().toISOString();
        const med = {
            id: id,
            medicationName: formData.medicationName,
            ndc: formData.ndc || null,
            sig: formData.sig,
            qty: parseInt(formData.qty, 10),
            unit: formData.unit || 'tablets',
            refills: parseInt(formData.refills, 10),
            refillsRemaining: parseInt(formData.refills, 10),
            daysSupply: parseInt(formData.daysSupply, 10) || 30,
            dispenseAsWritten: formData.dispenseAsWritten || false,
            status: 'active',
            classification: formData.classification || 'permanent_rx',
            prescriberId: this.currentUser.id,
            prescriberName: this.currentUser.name,
            pharmacyId: formData.pharmacyId || null,
            pharmacyName: formData.pharmacyName || null,
            startDate: now.split('T')[0],
            lastPrescribedDate: now.split('T')[0],
            lastFilledDate: null,
            nextRefillDate: null,
            diagnosis: formData.diagnosis || [],
            isControlled: formData.isControlled || false,
            scheduleClass: formData.scheduleClass || null,
            instructionsToPharmacy: formData.instructionsToPharmacy || '',
            doNotFillBefore: formData.doNotFillBefore || null
        };

        if (formData.classification === 'temporary') {
            this.temporaryMeds.push(med);
        } else if (formData.classification === 'permanent_otc') {
            this.permanentOtcMeds.push(med);
        } else {
            this.permanentRxMeds.push(med);
        }
        this.notify();
        return med;
    },

    discontinueMed(medId, reason, details, discontinuedBy, sendCancelRequest) {
        const allLists = [
            { list: this.permanentRxMeds, name: 'permanentRxMeds' },
            { list: this.permanentOtcMeds, name: 'permanentOtcMeds' },
            { list: this.temporaryMeds, name: 'temporaryMeds' }
        ];

        for (const { list } of allLists) {
            const idx = list.findIndex(m => m.id === medId);
            if (idx !== -1) {
                const med = list.splice(idx, 1)[0];
                med.status = 'discontinued';
                med.classification = 'discontinued';
                med.discontinuedDate = new Date().toISOString().split('T')[0];
                med.discontinuedBy = discontinuedBy || this.currentUser.name;
                med.discontinueReason = reason;
                med.discontinueDetails = details || '';
                if (sendCancelRequest && med.pharmacyId) {
                    const cxlId = `cxl_${String(this._nextCxlId++).padStart(3, '0')}`;
                    this.canceledScripts.push({
                        id: cxlId,
                        medicationName: med.medicationName,
                        ndc: med.ndc,
                        sig: med.sig,
                        qty: med.qty,
                        refills: med.refills,
                        daysSupply: med.daysSupply,
                        status: 'canceled',
                        classification: 'canceled',
                        prescriberId: med.prescriberId,
                        prescriberName: med.prescriberName,
                        pharmacyId: med.pharmacyId,
                        pharmacyName: med.pharmacyName,
                        prescribedDate: med.lastPrescribedDate,
                        canceledDate: new Date().toISOString().split('T')[0],
                        cancelReason: 'Medication discontinued: ' + reason,
                        diagnosis: med.diagnosis
                    });
                }
                this.discontinuedMeds.push(med);
                this.notify();
                return true;
            }
        }
        return false;
    },

    approveRefillRequest(requestId, modifications) {
        const req = this.refillRequests.find(r => r.id === requestId);
        if (!req) return false;
        req.status = 'approved';
        req.processedDate = new Date().toISOString();
        req.processedBy = this.currentUser.name;
        if (modifications) {
            req.modifications = modifications;
        }
        // Update the medication's refill info
        if (req.patientMedId) {
            const med = this.getMedById(req.patientMedId);
            if (med) {
                med.lastPrescribedDate = new Date().toISOString().split('T')[0];
                if (modifications && modifications.refills !== undefined) {
                    med.refillsRemaining = modifications.refills;
                }
                if (modifications && modifications.sig) {
                    med.sig = modifications.sig;
                }
            }
        }
        this.notify();
        return true;
    },

    denyRefillRequest(requestId, reason) {
        const req = this.refillRequests.find(r => r.id === requestId);
        if (!req) return false;
        req.status = 'denied';
        req.processedDate = new Date().toISOString();
        req.processedBy = this.currentUser.name;
        req.denyReason = reason || '';
        this.notify();
        return true;
    },

    approveChangeRequest(requestId) {
        const req = this.changeRequests.find(r => r.id === requestId);
        if (!req) return false;
        req.status = 'approved';
        req.processedDate = new Date().toISOString();
        req.processedBy = this.currentUser.name;
        this.notify();
        return true;
    },

    denyChangeRequest(requestId, reason) {
        const req = this.changeRequests.find(r => r.id === requestId);
        if (!req) return false;
        req.status = 'denied';
        req.processedDate = new Date().toISOString();
        req.processedBy = this.currentUser.name;
        req.denyReason = reason || '';
        this.notify();
        return true;
    },

    addRxTemplate(template) {
        const id = `tpl_${String(this._nextTplId++).padStart(3, '0')}`;
        const tpl = {
            id: id,
            medicationName: template.medicationName,
            sig: template.sig,
            qty: parseInt(template.qty, 10),
            unit: template.unit || 'tablets',
            refills: parseInt(template.refills, 10),
            daysSupply: parseInt(template.daysSupply, 10) || 30,
            ndc: template.ndc || null,
            createdDate: new Date().toISOString().split('T')[0]
        };
        this.rxTemplates.push(tpl);
        this.notify();
        return tpl;
    },

    updateRxTemplate(templateId, updates) {
        const tpl = this.rxTemplates.find(t => t.id === templateId);
        if (!tpl) return false;
        Object.assign(tpl, updates);
        this.notify();
        return true;
    },

    deleteRxTemplate(templateId) {
        const idx = this.rxTemplates.findIndex(t => t.id === templateId);
        if (idx === -1) return false;
        this.rxTemplates.splice(idx, 1);
        this.notify();
        return true;
    },

    addCustomSig(text, category) {
        const id = `sig_${String(this._nextSigId++).padStart(3, '0')}`;
        this.customSigs.push({ id, text, category: category || 'oral' });
        this.notify();
    },

    deleteCustomSig(sigId) {
        const idx = this.customSigs.findIndex(s => s.id === sigId);
        if (idx === -1) return false;
        this.customSigs.splice(idx, 1);
        this.notify();
        return true;
    },

    updateCustomSig(sigId, text, category) {
        const sig = this.customSigs.find(s => s.id === sigId);
        if (!sig) return false;
        sig.text = text;
        if (category) sig.category = category;
        this.notify();
        return true;
    },

    updateSettings(key, value) {
        if (key.includes('.')) {
            const parts = key.split('.');
            let obj = this.settings;
            for (let i = 0; i < parts.length - 1; i++) {
                obj = obj[parts[i]];
            }
            obj[parts[parts.length - 1]] = value;
        } else {
            this.settings[key] = value;
        }
        this.notify();
    },

    addAllergy(allergen, reaction, severity, type) {
        const id = `alg_${String(this._nextAlgId++).padStart(3, '0')}`;
        this.currentPatient.allergies.push({
            id, allergen, reaction, severity: severity || 'Unknown', type: type || 'drug',
            onsetDate: new Date().toISOString().split('T')[0], source: 'provider-entered'
        });
        this.notify();
    },

    removeAllergy(allergyId) {
        const idx = this.currentPatient.allergies.findIndex(a => a.id === allergyId);
        if (idx === -1) return false;
        this.currentPatient.allergies.splice(idx, 1);
        this.notify();
        return true;
    },

    updateLastReconciled() {
        this.currentPatient.lastReconciledDate = new Date().toISOString();
        this.notify();
    },

    setMedClassification(medId, newClassification) {
        const allLists = [
            { list: this.permanentRxMeds, cls: 'permanent_rx' },
            { list: this.permanentOtcMeds, cls: 'permanent_otc' },
            { list: this.temporaryMeds, cls: 'temporary' }
        ];
        for (const { list, cls } of allLists) {
            const idx = list.findIndex(m => m.id === medId);
            if (idx !== -1 && cls !== newClassification) {
                const med = list.splice(idx, 1)[0];
                med.classification = newClassification;
                if (newClassification === 'permanent_rx') this.permanentRxMeds.push(med);
                else if (newClassification === 'permanent_otc') this.permanentOtcMeds.push(med);
                else if (newClassification === 'temporary') this.temporaryMeds.push(med);
                this.notify();
                return true;
            }
        }
        return false;
    },

    documentMedication(formData) {
        const now = new Date().toISOString();
        const id = formData.type === 'otc' ?
            `otc_${String(this._nextOtcId++).padStart(3, '0')}` :
            `prx_${String(this._nextPrxId++).padStart(3, '0')}`;
        const med = {
            id: id,
            medicationName: formData.medicationName,
            ndc: formData.ndc || null,
            sig: formData.sig || '',
            qty: parseInt(formData.qty, 10) || 0,
            unit: formData.unit || 'tablets',
            refills: 0,
            refillsRemaining: 0,
            daysSupply: parseInt(formData.daysSupply, 10) || 30,
            dispenseAsWritten: false,
            status: 'active',
            classification: formData.type === 'otc' ? 'permanent_otc' : 'permanent_rx',
            prescriberId: null,
            prescriberName: null,
            pharmacyId: null,
            pharmacyName: null,
            startDate: formData.startDate || now.split('T')[0],
            lastPrescribedDate: null,
            documentedDate: now.split('T')[0],
            diagnosis: formData.diagnosis || [],
            isControlled: false,
            scheduleClass: null
        };

        if (formData.type === 'otc') {
            this.permanentOtcMeds.push(med);
        } else {
            this.permanentRxMeds.push(med);
        }
        this.notify();
        return med;
    },

    updateMedSig(medId, newSig) {
        const med = this.getMedById(medId);
        if (!med) return false;
        med.sig = newSig;
        this.notify();
        return true;
    }
};
