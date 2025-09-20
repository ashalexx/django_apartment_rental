// Функции для открытия и закрытия модальных окон
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'flex';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Закрытие модального окна при клике вне его области
window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

// Функция сохранения изменений (заглушка)
function saveChanges() {
    alert('Изменения сохранены!');
    closeModal('editModal');
}

// Функция удаления профиля (заглушка)
function deleteProfile() {
    alert('Профиль удален!');
    closeModal('deleteModal');
}