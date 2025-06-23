import React, { useState, useEffect } from "react";
import { fetchStudents } from "./services/api";
import FilterForm from "./FilterForm";
import Pagination from "./Pagination";
import "./styles/main.css"; // Import CSS

function App() {
  const [students, setStudents] = useState([]); // Danh sách sinh viên
  const [filters, setFilters] = useState({}); // Bộ lọc
  const [page, setPage] = useState(1); // Trang hiện tại
  const [totalStudents, setTotalStudents] = useState(0); // Tổng số sinh viên
  const [loading, setLoading] = useState(false); // Trạng thái loading
  const [error, setError] = useState(null); // Trạng thái lỗi

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true); // Bắt đầu loading
      setError(null); // Xóa lỗi cũ
      try {
        console.log("Fetching data with filters:", filters, "and page:", page); // Debug
        const response = await fetchStudents(page, filters); // Gọi API
        console.log("API Response:", response); // Debug dữ liệu trả về
        if (response && Array.isArray(response.students)) {
          setStudents(response.students); // Cập nhật danh sách sinh viên
          setTotalStudents(response.total); // Cập nhật tổng số sinh viên
        } else {
          throw new Error("Dữ liệu không hợp lệ");
        }
      } catch (error) {
        console.error("Error fetching students:", error);
        setError("Không thể tải dữ liệu. Vui lòng thử lại sau."); // Ghi nhận lỗi
      } finally {
        setLoading(false); // Kết thúc loading
      }
    };
    fetchData();
  }, [page, filters]);

  const totalPages = Math.ceil(totalStudents / 10); // Tính tổng số trang

  return (
    <div className="container">
      <header className="header">
        <h1>Danh sách sinh viên</h1>
        <p>
          Tổng số sinh viên : <strong>{totalStudents}</strong>
        </p>
      </header>
      <FilterForm setFilters={setFilters} />
      {loading ? (
        <p className="loading">Đang tải dữ liệu...</p>
      ) : error ? (
        <p className="error">{error}</p> // Hiển thị lỗi nếu có
      ) : (
        <table className="student-table">
          <thead>
            <tr>
              <th>Фамилия</th>
              <th>Имя</th>
              <th>Отчество</th>
              <th>Курс</th>
              <th>Группа</th>
              <th>Факультет</th>
            </tr>
          </thead>
          <tbody>
            {Array.isArray(students) && students.length > 0 ? (
              students.map((student) => (
                <tr key={student.id}>
                  <td>{student.Фамилия}</td>
                  <td>{student.Имя}</td>
                  <td>{student.Отчество}</td>
                  <td>{student.Курс}</td>
                  <td>{student.Группа}</td>
                  <td>{student.Факультет}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6">Không có dữ liệu</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
      <Pagination currentPage={page} setPage={setPage} totalPages={totalPages} />
    </div>
  );
}

export default App;
