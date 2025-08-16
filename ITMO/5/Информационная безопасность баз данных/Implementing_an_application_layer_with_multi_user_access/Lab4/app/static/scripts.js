// Làm mới trang
function refreshPage() {
    window.location.reload();
}

// Làm trống kết quả
function clearResult() {
    const queryInput = document.getElementById("query");
    if (queryInput) queryInput.value = "";

    const table = document.querySelector("table");
    if (table) table.remove();

    const errorMessage = document.querySelector("p[style='color: red;']");
    if (errorMessage) errorMessage.remove();
}

// Hiển thị thông báo khi nút được nhấn
function showMessage(message) {
    alert(message);
}
