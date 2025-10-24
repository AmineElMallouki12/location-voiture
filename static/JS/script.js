// Inventory Management System JavaScript

// Global variables
let currentItemId = null;

// Initialize when document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Dark/Light mode toggle
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        const icon = document.getElementById('themeToggleIcon');
        if (icon) {
            if (theme === 'dark') {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        }
    }
    function toggleTheme() {
        const current = localStorage.getItem('theme') || 'light';
        setTheme(current === 'dark' ? 'light' : 'dark');
    }
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
    const btn = document.getElementById('themeToggleBtn');
    if (btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            toggleTheme();
        });
    }
});

// Edit item function
function editItem(itemId) {
    currentItemId = itemId;
    
    // Fetch item data
    fetch(`/api/item/${itemId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const item = data.item;
                
                // Populate modal form
                document.querySelector('#editItemForm input[name="name"]').value = item.name;
                document.querySelector('#editItemForm select[name="condition"]').value = item.condition;
                document.querySelector('#editItemForm select[name="status"]').value = item.status;
                document.querySelector('#editItemForm textarea[name="notes"]').value = item.notes || '';
                
                // Show modal
                const modal = new bootstrap.Modal(document.getElementById('editItemModal'));
                modal.show();
            } else {
                showAlert('Error loading item data', 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showAlert('Error loading item data', 'danger');
        });
}

// Save item changes
function saveItem() {
    if (!currentItemId) return;
    
    const form = document.getElementById('editItemForm');
    const formData = new FormData(form);
    
    fetch(`/api/item/${currentItemId}`, {
        method: 'PUT',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert('Item updated successfully', 'success');
            // Close modal
            const modal = bootstrap.Modal.getInstance(document.getElementById('editItemModal'));
            modal.hide();
            // Reload page to show updated data
            setTimeout(() => location.reload(), 1000);
        } else {
            showAlert(data.message || 'Error updating item', 'danger');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showAlert('Error updating item', 'danger');
    });
}

// View item details
function viewItem(itemId) {
    fetch(`/api/item/${itemId}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const item = data.item;
                showItemDetails(item);
            } else {
                showAlert('Error loading item details', 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showAlert('Error loading item details', 'danger');
        });
}

// Show item details in modal
function showItemDetails(item) {
    const modalHtml = `
        <div class="modal fade" id="itemDetailsModal" tabindex="-1">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">
                            <i class="fas fa-box me-2"></i>${item.designation}
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col-md-6">
                                <p><strong>ID:</strong> ${item.id}</p>
                                <p><strong>Marque:</strong> ${item.marque}</p>
                                <p><strong>Modèle:</strong> ${item.modele}</p>
                                <p><strong>N° Série:</strong> ${item.n_serie}</p>
                                <p><strong>Ancien CAB:</strong> ${item.ancien_cab}</p>
                                <p><strong>Nouveau CAB:</strong> ${item.nouveau_cab}</p>
                            </div>
                            <div class="col-md-6">
                                <p><strong>État:</strong> ${item.etat}</p>
                                <p><strong>Date d’inventaire:</strong> ${item.date_inv}</p>
                                <p><strong>Description / Observation:</strong> ${item.description}</p>
                                <p><strong>Créé:</strong> ${item.created_at || 'N/A'}</p>
                                <p><strong>Dernière modification:</strong> ${item.updated_at || 'N/A'}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    const modal = new bootstrap.Modal(document.getElementById('itemDetailsModal'));
    modal.show();
    document.getElementById('itemDetailsModal').addEventListener('hidden.bs.modal', function () {
        document.getElementById('itemDetailsModal').remove();
    });
}

// Delete item
function deleteItem(itemId) {
    if (confirm('Are you sure you want to delete this item? This action cannot be undone.')) {
        fetch(`/api/item/${itemId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showAlert('Item deleted successfully', 'success');
                // Remove row from table
                const row = document.querySelector(`tr[data-item-id="${itemId}"]`);
                if (row) row.remove();
            } else {
                showAlert(data.message || 'Error deleting item', 'danger');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showAlert('Error deleting item', 'danger');
        });
    }
}

// Helper functions
function getConditionBadgeClass(condition) {
    switch(condition) {
        case 'Good': return 'bg-success';
        case 'Needs Repair': return 'bg-warning text-dark';
        case 'Bad': return 'bg-danger';
        default: return 'bg-secondary';
    }
}

function getStatusBadgeClass(status) {
    if (!status) return 'bg-secondary';
    
    const statusLower = status.toLowerCase();
    if (statusLower.includes('disponible')) return 'bg-success';
    if (statusLower.includes('indisponible')) return 'bg-danger';
    if (statusLower.includes('cassé') || statusLower.includes('cassée')) return 'bg-danger';
    if (statusLower.includes('en réparation')) return 'bg-warning text-dark';
    if (statusLower.includes('nécessite une réparation')) return 'bg-warning text-dark';
    if (statusLower.includes('perdue')) return 'bg-dark';
    if (statusLower.includes('en attente')) return 'bg-warning text-dark';
    if (statusLower.includes('approuvée par professeur')) return 'bg-info';
    if (statusLower.includes('approved')) return 'bg-success';
    if (statusLower.includes('rejected') || statusLower.includes('rejetée')) return 'bg-danger';
    if (statusLower.includes('active')) return 'bg-primary';
    if (statusLower.includes('completed')) return 'bg-secondary';
    
    return 'bg-secondary';
}

function createStatusBadge(status) {
    if (!status) return '<span class="badge bg-secondary">N/A</span>';
    
    const badgeClass = getStatusBadgeClass(status);
    return `<span class="badge ${badgeClass}">${status}</span>`;
}

function showAlert(message, type) {
    const alertHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    // Add alert to page
    const container = document.querySelector('.main-container');
    container.insertAdjacentHTML('afterbegin', alertHtml);
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        const alert = document.querySelector('.alert');
        if (alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }
    }, 5000);
}

// Search functionality
function searchItems() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const rows = document.querySelectorAll('tbody tr');
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(searchTerm) ? '' : 'none';
    });
}

// Filter functionality
function filterItems(filter) {
    const table = document.querySelector('table');
    if (!table) return;
    const headers = Array.from(table.querySelectorAll('thead th'));
    let statusColIdx = headers.findIndex(th => th.textContent.trim().toLowerCase().includes('statut'));
    if (statusColIdx === -1) statusColIdx = 0; // fallback

    const rows = document.querySelectorAll('tbody tr');
    let visibleCount = 0;

    rows.forEach(row => {
        // Skip the "no items found" row
        if (row.querySelector('td[colspan]')) {
            return;
        }
        const cells = row.querySelectorAll('td');
        const statusCell = cells[statusColIdx];
        const statusBadge = statusCell ? statusCell.querySelector('.badge') : null;
        const status = statusBadge ? statusBadge.textContent.trim().toLowerCase() : (statusCell ? statusCell.textContent.trim().toLowerCase() : '');

        let show = true;
        if (filter === 'available') {
            show = status.includes('disponible');
        } else if (filter === 'unavailable') {
            show = status.includes('indisponible');
        } else if (filter === 'broken') {
            show = status.includes('cassé') || status.includes('cassée');
        } else if (filter === 'repair') {
            show = status.includes('en réparation');
        } else if (filter === 'needs_repair') {
            show = status.includes('nécessite une réparation');
        } else if (filter === 'all') {
            show = true;
        }

        row.style.display = show ? '' : 'none';
        if (show) visibleCount++;
    });
}

// Export functionality (detailed, category-aware)
function exportData(format) {
    // Collect all category tables
    const tables = document.querySelectorAll('.category-block table');
    const records = [];

    const normalize = (t) => (t || '').replace(/\s+/g, ' ').trim();
    const normalizeHeader = (t) => normalize(t).toLowerCase();

    tables.forEach(table => {
        const block = table.closest('.category-block');
        const categoryTitle = block ? normalize(block.querySelector('.card-header h5')?.textContent || '') : '';
        const headerCells = Array.from(table.querySelectorAll('thead th'));
        const headerIdx = {};
        headerCells.forEach((th, idx) => {
            const h = normalizeHeader(th.textContent);
            headerIdx[h] = idx;
        });

        // Helper to find a column index by fuzzy header text
        const findIdx = (candidates) => {
            for (const key of candidates) {
                for (const h in headerIdx) {
                    if (h.includes(key)) return headerIdx[h];
                }
            }
            return -1;
        };

        const idx = {
            id: findIdx(['id']),
            designation: findIdx(['désignation', 'designation']),
            marque: findIdx(['marque']),
            modele: findIdx(['modèle', 'modele']),
            n_serie: findIdx(['n° série', 'n°', 'serie']),
            ancien_cab: findIdx(['ancien cab']),
            nouveau_cab: findIdx(['nouveau cab']),
            date_inv: findIdx(["date d'inventaire", 'date d’', 'date d']),
            qte_totale: findIdx(['quantité totale']),
            qte_disponible: findIdx(['disponible']),
            qte_cassee: findIdx(['cassée', 'cassee']),
            qte_reparation: findIdx(['en réparation', 'reparation']),
            statut: findIdx(['statut']),
            etat: findIdx(['état', 'etat']),
            description: findIdx(['description'])
        };

        const rows = Array.from(table.querySelectorAll('tbody tr'));
        rows.forEach(row => {
            // Skip placeholder rows
            if (row.querySelector('td[colspan]')) return;
            const cells = Array.from(row.querySelectorAll('td'));
            if (cells.length === 0) return;
            const getText = (i) => i >= 0 && cells[i] ? normalize(cells[i].innerText || cells[i].textContent) : '';
            const getStatus = (i) => {
                if (i < 0 || !cells[i]) return '';
                const badge = cells[i].querySelector('.badge');
                return normalize(badge ? badge.textContent : cells[i].innerText || cells[i].textContent);
            };

            records.push({
                'Catégorie': categoryTitle,
                'ID': getText(idx.id),
                'Désignation': getText(idx.designation),
                'Marque': getText(idx.marque),
                'Modèle': getText(idx.modele),
                'N° Série': getText(idx.n_serie),
                'Ancien CAB': getText(idx.ancien_cab),
                'Nouveau CAB': getText(idx.nouveau_cab),
                "Date d’inventaire": getText(idx.date_inv),
                'Quantité Totale': getText(idx.qte_totale),
                'Disponible': getText(idx.qte_disponible),
                'Cassée': getText(idx.qte_cassee),
                'En Réparation': getText(idx.qte_reparation),
                'Statut': getStatus(idx.statut),
                'État': getText(idx.etat),
                'Description / Observation': getText(idx.description)
            });
        });
    });

    if (format === 'csv') {
        exportToCSV(records);
    } else if (format === 'json') {
        exportToJSON(records);
    }
}

function exportToCSV(rows) {
    if (!rows || rows.length === 0) {
        downloadFile('\uFEFF', 'inventory.csv', 'text/csv;charset=utf-8');
        return;
    }
    const headers = Object.keys(rows[0]);
    const needsTextCoercion = (header, value) => {
        const h = (header || '').toLowerCase();
        const v = String(value == null ? '' : value);
        const longDigits = /^\d{11,}$/.test(v); // long numeric strings
        const looksSci = /e\+\d+$/i.test(v);
        const sensitiveColumn = (
            h.includes('cab') || h.includes('n°') || h.includes('n\u00b0') || h.includes('série') || h.includes('serie') || h === 'id'
        );
        return longDigits || looksSci || sensitiveColumn;
    };
    const escapeCsv = (val, header) => {
        const s = (val == null ? '' : String(val));
        const coerced = needsTextCoercion(header, s) ? "'" + s : s; // leading apostrophe forces text in Excel
        const out = coerced;
        if (out.includes('"') || out.includes(',') || out.includes('\n')) {
            return '"' + out.replace(/"/g, '""') + '"';
        }
        return out;
    };
    const sep = ';';
    const csvContent = [
        headers.join(sep),
        ...rows.map(r => headers.map(h => escapeCsv(r[h], h)).join(sep))
    ].join('\n');
    // Prepend BOM to force UTF-8 in Excel (FR locales often expect ';' as separator)
    downloadFile('\uFEFF' + csvContent, 'inventory.csv', 'text/csv;charset=utf-8');
}

function exportToJSON(rows) {
    const jsonContent = JSON.stringify(rows, null, 2);
    downloadFile(jsonContent, 'inventory.json', 'application/json');
}

function downloadFile(content, filename, contentType) {
    const blob = new Blob([content], { type: contentType });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// Image validation helper
function validateImageInput(input) {
    const file = input.files[0];
    if (!file) return true;
    const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    if (!allowedTypes.includes(file.type)) {
        showAlert('Invalid image file type. Only JPG, PNG, GIF allowed.', 'danger');
        input.value = '';
        return false;
    }
    if (file.size > 2 * 1024 * 1024) {
        showAlert('Image file is too large (max 2MB).', 'danger');
        input.value = '';
        return false;
    }
    return true;
}

// Add validation to add item form
const addItemForm = document.getElementById('addItemForm');
if (addItemForm) {
    addItemForm.addEventListener('submit', function(e) {
        const imageInput = addItemForm.querySelector('input[name="image"]');
        if (imageInput && !validateImageInput(imageInput)) {
            e.preventDefault();
            return false;
        }
    });
}

// Add validation to edit item form (modal)
const editItemForm = document.getElementById('editItemForm');
if (editItemForm) {
    editItemForm.addEventListener('submit', function(e) {
        const imageInput = editItemForm.querySelector('input[name="image"]');
        if (imageInput && !validateImageInput(imageInput)) {
            e.preventDefault();
            return false;
        }
    });
}
