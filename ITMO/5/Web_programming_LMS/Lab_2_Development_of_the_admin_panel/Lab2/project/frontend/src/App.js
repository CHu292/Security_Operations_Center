import React, { useState, useEffect } from "react";
import { fetchStudents } from "./services/api";
import FilterForm from "./FilterForm";
import Pagination from "./Pagination";
import "./styles/main.css";

function App() {
  const [students, setStudents] = useState([]);
  const [filters, setFilters] = useState({});
  const [page, setPage] = useState(1);
  const [totalStudents, setTotalStudents] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await fetchStudents(page, filters);
        if (response && Array.isArray(response.students)) {
          setStudents(response.students);
          setTotalStudents(response.total);
        } else {
          throw new Error("Неверные данные");
        }
      } catch (error) {
        setError("Не удалось загрузить данные. Попробуйте позже.");
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [page, filters]);

  const totalPages = Math.ceil(totalStudents / 10);

  return (
    <div className="container">
      <header className="header">
        <h1>Список студентов</h1>
        <p>
          Всего студентов: <strong>{totalStudents}</strong>
        </p>
      </header>
      <FilterForm setFilters={setFilters} />
      {loading ? (
        <p className="loading">Загрузка данных...</p>
      ) : error ? (
        <p className="error">{error}</p>
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
                <td colSpan="6">Нет данных</td>
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
