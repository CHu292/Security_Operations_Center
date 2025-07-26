import React, { useState } from "react";
import "./styles/main.css"; // Import CSS

function FilterForm({ setFilters }) {
  const [localFilters, setLocalFilters] = useState({});

  const handleChange = (e) => {
    setLocalFilters({ ...localFilters, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Chỉ gửi các bộ lọc không rỗng
    const validFilters = Object.fromEntries(
      Object.entries(localFilters).filter(([key, value]) => value.trim() !== "")
    );
    setFilters(validFilters);
  };

  const handleClear = () => {
    setLocalFilters({});
    setFilters({});
  };

  return (
    <form className="filter-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <label htmlFor="Фамилия">Фамилия:</label>
        <input
          id="Фамилия"
          name="Фамилия"
          placeholder="Nhập họ"
          value={localFilters["Фамилия"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Имя">Имя:</label>
        <input
          id="Имя"
          name="Имя"
          placeholder="Nhập tên"
          value={localFilters["Имя"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Отчество">Отчество:</label>
        <input
          id="Отчество"
          name="Отчество"
          placeholder="Nhập tên đệm"
          value={localFilters["Отчество"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Курс">Курс:</label>
        <input
          id="Курс"
          name="Курс"
          placeholder="Nhập khóa học"
          value={localFilters["Курс"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Группа">Группа:</label>
        <input
          id="Группа"
          name="Группа"
          placeholder="Nhập nhóm"
          value={localFilters["Группа"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Факультет">Факультет:</label>
        <input
          id="Факультет"
          name="Факультет"
          placeholder="Nhập khoa"
          value={localFilters["Факультет"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-actions">
        <button className="btn btn-submit" type="submit">
          Apply Filters
        </button>
        <button
          className="btn btn-clear"
          type="button"
          onClick={handleClear}
        >
          Clear Filters
        </button>
      </div>
    </form>
  );
}

export default FilterForm;
