// ============================================================
// state.js — Centralized state management with localStorage persistence
// ============================================================

const STORAGE_KEY = 'shopifyWebPerfAppState';

function _loadSeedData() {
    return {
        _seedVersion: SEED_DATA_VERSION,
        store: JSON.parse(JSON.stringify(STORE)),
        currentUser: JSON.parse(JSON.stringify(CURRENT_USER)),
        themes: JSON.parse(JSON.stringify(THEMES)),
        apps: JSON.parse(JSON.stringify(APPS)),
        pages: JSON.parse(JSON.stringify(PAGES)),
        performanceRecords: JSON.parse(JSON.stringify(PERFORMANCE_RECORDS)),
        events: JSON.parse(JSON.stringify(EVENTS)),
        performanceBudgets: JSON.parse(JSON.stringify(PERFORMANCE_BUDGETS)),
        alertRules: JSON.parse(JSON.stringify(ALERT_RULES)),
        optimizations: JSON.parse(JSON.stringify(OPTIMIZATIONS)),
        savedReports: JSON.parse(JSON.stringify(SAVED_REPORTS)),
        _nextThemeId: 7,
        _nextAppId: 11,
        _nextPageId: 13,
        _nextEventId: 9,
        _nextAlertId: 7,
        _nextOptimizationId: 9,
        _nextReportId: 5
    };
}

function _loadPersistedData() {
    try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (!raw) {
            console.log('[AppState] No persisted data found, using seed data');
            return null;
        }
        const parsed = JSON.parse(raw);
        if (parsed._seedVersion !== SEED_DATA_VERSION) {
            console.log('[AppState] Seed data version changed, discarding stale localStorage');
            localStorage.removeItem(STORAGE_KEY);
            return null;
        }
        console.log('[AppState] Loaded persisted data');
        return parsed;
    } catch (e) {
        console.error('[AppState] Failed to load persisted data:', e);
        return null;
    }
}

const _initial = _loadPersistedData() || _loadSeedData();

const AppState = {
    // Data collections
    store: _initial.store,
    currentUser: _initial.currentUser,
    themes: _initial.themes,
    apps: _initial.apps,
    pages: _initial.pages,
    performanceRecords: _initial.performanceRecords,
    events: _initial.events,
    performanceBudgets: _initial.performanceBudgets,
    alertRules: _initial.alertRules,
    optimizations: _initial.optimizations,
    savedReports: _initial.savedReports,

    // Seed data version
    _seedVersion: _initial._seedVersion,

    // UI state (transient — not persisted)
    currentRoute: '/',
    routeParams: {},
    sidebarOpen: true,
    modalOpen: false,
    validationErrors: {},
    toasts: [],

    // Auto-increment counters
    _nextThemeId: _initial._nextThemeId,
    _nextAppId: _initial._nextAppId,
    _nextPageId: _initial._nextPageId,
    _nextEventId: _initial._nextEventId,
    _nextAlertId: _initial._nextAlertId,
    _nextOptimizationId: _initial._nextOptimizationId,
    _nextReportId: _initial._nextReportId,

    // Listeners
    _listeners: [],

    subscribe(fn) {
        this._listeners.push(fn);
        return () => {
            this._listeners = this._listeners.filter(l => l !== fn);
        };
    },

    notify() {
        this._listeners.forEach(fn => fn(this));
        this._persist();
    },

    // ---- Persistence ----

    _getPersistable() {
        return {
            _seedVersion: this._seedVersion,
            store: this.store,
            currentUser: this.currentUser,
            themes: this.themes,
            apps: this.apps,
            pages: this.pages,
            performanceRecords: this.performanceRecords,
            events: this.events,
            performanceBudgets: this.performanceBudgets,
            alertRules: this.alertRules,
            optimizations: this.optimizations,
            savedReports: this.savedReports,
            _nextThemeId: this._nextThemeId,
            _nextAppId: this._nextAppId,
            _nextPageId: this._nextPageId,
            _nextEventId: this._nextEventId,
            _nextAlertId: this._nextAlertId,
            _nextOptimizationId: this._nextOptimizationId,
            _nextReportId: this._nextReportId
        };
    },

    _persist() {
        try {
            const persistable = this._getPersistable();
            const json = JSON.stringify(persistable);
            localStorage.setItem(STORAGE_KEY, json);
            fetch('/api/state', {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: json
            }).catch(() => {});
        } catch (e) {
            console.error('[AppState] Failed to persist state:', e);
        }
    },

    resetToSeedData() {
        localStorage.removeItem(STORAGE_KEY);
        const seed = _loadSeedData();
        this.store = seed.store;
        this.currentUser = seed.currentUser;
        this.themes = seed.themes;
        this.apps = seed.apps;
        this.pages = seed.pages;
        this.performanceRecords = seed.performanceRecords;
        this.events = seed.events;
        this.performanceBudgets = seed.performanceBudgets;
        this.alertRules = seed.alertRules;
        this.optimizations = seed.optimizations;
        this.savedReports = seed.savedReports;
        this._seedVersion = seed._seedVersion;
        this._nextThemeId = seed._nextThemeId;
        this._nextAppId = seed._nextAppId;
        this._nextPageId = seed._nextPageId;
        this._nextEventId = seed._nextEventId;
        this._nextAlertId = seed._nextAlertId;
        this._nextOptimizationId = seed._nextOptimizationId;
        this._nextReportId = seed._nextReportId;
        this._listeners.forEach(fn => fn(this));
        fetch('/api/state', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(this._getPersistable())
        }).catch(() => {});
    },

    // ---- Helper Methods ----

    getThemeById(id) {
        return this.themes.find(t => t.id === parseInt(id));
    },

    getActiveTheme() {
        return this.themes.find(t => t.active);
    },

    getAppById(id) {
        return this.apps.find(a => a.id === parseInt(id));
    },

    getInstalledApps() {
        return this.apps.filter(a => a.installed);
    },

    getAvailableApps() {
        return this.apps.filter(a => !a.installed);
    },

    getPageById(id) {
        return this.pages.find(p => p.id === parseInt(id));
    },

    getMonitoredPages() {
        return this.pages.filter(p => p.monitored);
    },

    getEventById(id) {
        return this.events.find(e => e.id === parseInt(id));
    },

    getAlertById(id) {
        return this.alertRules.find(a => a.id === parseInt(id));
    },

    getOptimizationById(id) {
        return this.optimizations.find(o => o.id === parseInt(id));
    },

    getSavedReportById(id) {
        return this.savedReports.find(r => r.id === parseInt(id));
    },

    // ---- Performance Data Queries ----

    getPerformanceForPage(pageId, dateRange, deviceType) {
        let records = this.performanceRecords.filter(r => r.pageId === parseInt(pageId));
        if (deviceType && deviceType !== 'all') {
            records = records.filter(r => r.deviceType === deviceType);
        }
        if (dateRange) {
            const now = new Date('2026-02-19');
            let startDate;
            if (dateRange === 'today') {
                startDate = new Date('2026-02-19');
            } else if (dateRange === 'last_7_days') {
                startDate = new Date(now);
                startDate.setDate(startDate.getDate() - 7);
            } else if (dateRange === 'last_30_days') {
                startDate = new Date(now);
                startDate.setDate(startDate.getDate() - 30);
            }
            if (startDate) {
                const startStr = startDate.toISOString().split('T')[0];
                records = records.filter(r => r.date >= startStr);
            }
        }
        return records;
    },

    getAggregateMetrics(dateRange, deviceType) {
        // Get p75 values across all monitored pages
        let records = this.performanceRecords.filter(r => {
            const page = this.getPageById(r.pageId);
            return page && page.monitored;
        });
        if (deviceType && deviceType !== 'all') {
            records = records.filter(r => r.deviceType === deviceType);
        }
        if (dateRange) {
            const now = new Date('2026-02-19');
            let startDate;
            if (dateRange === 'today') {
                startDate = new Date('2026-02-19');
            } else if (dateRange === 'last_7_days') {
                startDate = new Date(now);
                startDate.setDate(startDate.getDate() - 7);
            } else if (dateRange === 'last_30_days') {
                startDate = new Date(now);
                startDate.setDate(startDate.getDate() - 30);
            }
            if (startDate) {
                const startStr = startDate.toISOString().split('T')[0];
                records = records.filter(r => r.date >= startStr);
            }
        }

        if (records.length === 0) {
            return { lcp: null, inp: null, cls: null };
        }

        // Calculate P75 for each metric
        function p75(values) {
            if (values.length === 0) return null;
            const sorted = [...values].sort((a, b) => a - b);
            const idx = Math.ceil(sorted.length * 0.75) - 1;
            return sorted[Math.max(0, idx)];
        }

        return {
            lcp: p75(records.map(r => r.lcp)),
            inp: p75(records.map(r => r.inp)),
            cls: p75(records.map(r => r.cls))
        };
    },

    getRating(metric, value) {
        if (value === null || value === undefined) return 'unknown';
        const thresholds = METRIC_THRESHOLDS[metric.toUpperCase()];
        if (!thresholds) return 'unknown';
        if (value <= thresholds.good) return 'good';
        if (value < thresholds.moderate) return 'moderate';
        return 'poor';
    },

    getPerformanceByPageType(dateRange, deviceType) {
        const records = this.performanceRecords.filter(r => {
            const page = this.getPageById(r.pageId);
            return page && page.monitored;
        });
        const filtered = this._filterByDateAndDevice(records, dateRange, deviceType);

        const byType = {};
        filtered.forEach(r => {
            const page = this.getPageById(r.pageId);
            if (!page) return;
            if (!byType[page.type]) {
                byType[page.type] = { lcpValues: [], inpValues: [], clsValues: [], sessions: 0 };
            }
            byType[page.type].lcpValues.push(r.lcp);
            byType[page.type].inpValues.push(r.inp);
            byType[page.type].clsValues.push(r.cls);
            byType[page.type].sessions += r.sessions;
        });

        function p75(arr) {
            if (!arr.length) return null;
            const sorted = [...arr].sort((a, b) => a - b);
            return sorted[Math.ceil(sorted.length * 0.75) - 1];
        }

        return Object.entries(byType).map(([type, data]) => ({
            pageType: type,
            lcp: p75(data.lcpValues),
            inp: p75(data.inpValues),
            cls: p75(data.clsValues),
            sessions: data.sessions
        }));
    },

    getPerformanceByPageUrl(dateRange, deviceType) {
        const pages = this.getMonitoredPages();
        return pages.map(page => {
            const records = this._filterByDateAndDevice(
                this.performanceRecords.filter(r => r.pageId === page.id),
                dateRange, deviceType
            );
            function p75(arr) {
                if (!arr.length) return null;
                const sorted = [...arr].sort((a, b) => a - b);
                return sorted[Math.ceil(sorted.length * 0.75) - 1];
            }
            return {
                pageId: page.id,
                path: page.path,
                name: page.name,
                type: page.type,
                lcp: p75(records.map(r => r.lcp)),
                inp: p75(records.map(r => r.inp)),
                cls: p75(records.map(r => r.cls)),
                sessions: records.reduce((s, r) => s + r.sessions, 0)
            };
        });
    },

    getPerformanceOverTime(metric, dateRange, deviceType) {
        const records = this.performanceRecords.filter(r => {
            const page = this.getPageById(r.pageId);
            return page && page.monitored;
        });
        const filtered = this._filterByDateAndDevice(records, dateRange, deviceType);

        const byDate = {};
        filtered.forEach(r => {
            if (!byDate[r.date]) {
                byDate[r.date] = { values: [], sessions: 0, goodCount: 0, moderateCount: 0, poorCount: 0 };
            }
            byDate[r.date].values.push(r[metric]);
            byDate[r.date].sessions += r.sessions;
            if (metric === 'lcp') {
                byDate[r.date].goodCount += r.goodLcp;
                byDate[r.date].moderateCount += r.moderateLcp;
                byDate[r.date].poorCount += r.poorLcp;
            } else if (metric === 'inp') {
                byDate[r.date].goodCount += r.goodInp;
                byDate[r.date].moderateCount += r.moderateInp;
                byDate[r.date].poorCount += r.poorInp;
            } else if (metric === 'cls') {
                byDate[r.date].goodCount += r.goodCls;
                byDate[r.date].moderateCount += r.moderateCls;
                byDate[r.date].poorCount += r.poorCls;
            }
        });

        function p75(arr) {
            if (!arr.length) return null;
            const sorted = [...arr].sort((a, b) => a - b);
            return sorted[Math.ceil(sorted.length * 0.75) - 1];
        }

        return Object.keys(byDate).sort().map(date => {
            const d = byDate[date];
            const total = d.goodCount + d.moderateCount + d.poorCount;
            return {
                date,
                value: p75(d.values),
                sessions: d.sessions,
                good: total > 0 ? Math.round(d.goodCount / total * 100) : 0,
                moderate: total > 0 ? Math.round(d.moderateCount / total * 100) : 0,
                poor: total > 0 ? Math.round(d.poorCount / total * 100) : 0
            };
        });
    },

    _filterByDateAndDevice(records, dateRange, deviceType) {
        let filtered = [...records];
        if (deviceType && deviceType !== 'all') {
            filtered = filtered.filter(r => r.deviceType === deviceType);
        }
        if (dateRange) {
            const now = new Date('2026-02-19');
            let startDate;
            if (dateRange === 'today') {
                startDate = new Date('2026-02-18');
            } else if (dateRange === 'last_7_days') {
                startDate = new Date(now);
                startDate.setDate(startDate.getDate() - 7);
            } else if (dateRange === 'last_30_days') {
                startDate = new Date(now);
                startDate.setDate(startDate.getDate() - 30);
            }
            if (startDate) {
                const startStr = startDate.toISOString().split('T')[0];
                filtered = filtered.filter(r => r.date >= startStr);
            }
        }
        return filtered;
    },

    // ---- Mutation Methods ----

    // Store
    updateStore(data) {
        Object.assign(this.store, data);
        this.notify();
    },

    // Themes
    activateTheme(themeId) {
        this.themes.forEach(t => t.active = false);
        const theme = this.getThemeById(themeId);
        if (theme) theme.active = true;
        this.notify();
    },

    updateThemeSettings(themeId, settings) {
        const theme = this.getThemeById(themeId);
        if (theme) {
            Object.assign(theme.settings, settings);
            this.notify();
        }
    },

    // Apps
    installApp(appId) {
        const app = this.getAppById(appId);
        if (app) {
            app.installed = true;
            app.installedAt = new Date().toISOString();
            app.status = 'active';
            this.notify();
        }
    },

    uninstallApp(appId) {
        const app = this.getAppById(appId);
        if (app) {
            app.installed = false;
            app.installedAt = null;
            app.status = 'available';
            this.notify();
        }
    },

    updateAppSettings(appId, settings) {
        const app = this.getAppById(appId);
        if (app) {
            Object.assign(app.settings, settings);
            this.notify();
        }
    },

    // Pages
    addPage(data) {
        const id = this._nextPageId++;
        this.pages.push({
            id,
            path: data.path,
            name: data.name,
            type: data.type,
            monitored: data.monitored !== undefined ? data.monitored : true,
            priority: data.priority || 'medium'
        });
        this.notify();
        return id;
    },

    updatePage(pageId, data) {
        const page = this.getPageById(pageId);
        if (page) {
            Object.assign(page, data);
            this.notify();
        }
    },

    removePage(pageId) {
        this.pages = this.pages.filter(p => p.id !== parseInt(pageId));
        this.performanceRecords = this.performanceRecords.filter(r => r.pageId !== parseInt(pageId));
        this.notify();
    },

    togglePageMonitoring(pageId) {
        const page = this.getPageById(pageId);
        if (page) {
            page.monitored = !page.monitored;
            this.notify();
        }
    },

    // Events
    addEvent(data) {
        const id = this._nextEventId++;
        this.events.push({
            id,
            date: data.date || new Date().toISOString(),
            type: data.type || 'custom',
            title: data.title,
            description: data.description || '',
            metric: data.metric || 'all',
            impact: data.impact || 'neutral'
        });
        this.notify();
        return id;
    },

    updateEvent(eventId, data) {
        const event = this.getEventById(eventId);
        if (event) {
            Object.assign(event, data);
            this.notify();
        }
    },

    removeEvent(eventId) {
        this.events = this.events.filter(e => e.id !== parseInt(eventId));
        this.notify();
    },

    // Performance Budgets
    updateBudget(metric, data) {
        if (this.performanceBudgets[metric]) {
            Object.assign(this.performanceBudgets[metric], data);
            this.notify();
        }
    },

    // Alert Rules
    addAlertRule(data) {
        const id = this._nextAlertId++;
        this.alertRules.push({
            id,
            name: data.name,
            metric: data.metric,
            condition: data.condition || 'greater_than',
            threshold: data.threshold,
            pageType: data.pageType || 'all',
            deviceType: data.deviceType || 'all',
            enabled: data.enabled !== undefined ? data.enabled : true,
            notifyEmail: data.notifyEmail !== undefined ? data.notifyEmail : true,
            createdAt: new Date().toISOString()
        });
        this.notify();
        return id;
    },

    updateAlertRule(alertId, data) {
        const rule = this.getAlertById(alertId);
        if (rule) {
            Object.assign(rule, data);
            this.notify();
        }
    },

    removeAlertRule(alertId) {
        this.alertRules = this.alertRules.filter(a => a.id !== parseInt(alertId));
        this.notify();
    },

    toggleAlertRule(alertId) {
        const rule = this.getAlertById(alertId);
        if (rule) {
            rule.enabled = !rule.enabled;
            this.notify();
        }
    },

    // Optimizations
    addOptimization(data) {
        const id = this._nextOptimizationId++;
        this.optimizations.push({
            id,
            title: data.title,
            description: data.description || '',
            metric: data.metric,
            priority: data.priority || 'medium',
            status: data.status || 'pending',
            estimatedImpact: data.estimatedImpact || '',
            category: data.category || 'other',
            pageAffected: data.pageAffected || '*',
            createdAt: new Date().toISOString()
        });
        this.notify();
        return id;
    },

    updateOptimization(optId, data) {
        const opt = this.getOptimizationById(optId);
        if (opt) {
            Object.assign(opt, data);
            this.notify();
        }
    },

    removeOptimization(optId) {
        this.optimizations = this.optimizations.filter(o => o.id !== parseInt(optId));
        this.notify();
    },

    // Saved Reports
    addSavedReport(data) {
        const id = this._nextReportId++;
        this.savedReports.push({
            id,
            name: data.name,
            metric: data.metric,
            reportType: data.reportType,
            filters: {
                deviceType: data.filters?.deviceType || 'all',
                dateRange: data.filters?.dateRange || 'last_30_days',
                pageType: data.filters?.pageType || 'all'
            },
            createdAt: new Date().toISOString()
        });
        this.notify();
        return id;
    },

    updateSavedReport(reportId, data) {
        const report = this.getSavedReportById(reportId);
        if (report) {
            if (data.name) report.name = data.name;
            if (data.metric) report.metric = data.metric;
            if (data.reportType) report.reportType = data.reportType;
            if (data.filters) Object.assign(report.filters, data.filters);
            this.notify();
        }
    },

    removeSavedReport(reportId) {
        this.savedReports = this.savedReports.filter(r => r.id !== parseInt(reportId));
        this.notify();
    }
};
