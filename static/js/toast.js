function showToast(title, message, type = 'normal') {
    const toast = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');

    if (!toast) return;

    // Set isi judul dan pesan
    if (toastTitle) toastTitle.textContent = title;
    if (toastMessage) toastMessage.textContent = message;

    // Atur class CSS untuk tipe (success/error/normal) dan animasi
    toast.className = `toast-component toast-${type} toast-show`;

    // Tampilkan popover menggunakan Native HTML Popover API
    if (typeof toast.showPopover === 'function') {
        toast.showPopover();
    }

    // Sembunyikan otomatis setelah 3 detik
    setTimeout(() => {
        toast.classList.remove('toast-show');
        toast.classList.add('toast-hidden');

        setTimeout(() => {
            if (typeof toast.hidePopover === 'function') {
                toast.hidePopover();
            }
        }, 300); // Waktu jeda transisi fade out
    }, 3000);
}