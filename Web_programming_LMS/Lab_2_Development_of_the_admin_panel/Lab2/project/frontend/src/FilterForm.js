import React, { useState } from "react";
import "./styles/main.css";

function FilterForm({ setFilters }) {
  const [localFilters, setLocalFilters] = useState({});

  const handleChange = (e) => {
    setLocalFilters({ ...localFilters, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
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
          placeholder="Введите фамилию"
          value={localFilters["Фамилия"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Имя">Имя:</label>
        <input
          id="Имя"
          name="Имя"
          placeholder="Введите имя"
          value={localFilters["Имя"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Отчество">Отчество:</label>
        <input
          id="Отчество"
          name="Отчество"
          placeholder="Введите отчество"
          value={localFilters["Отчество"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Курс">Курс:</label>
        <input
          id="Курс"
          name="Курс"
          placeholder="Введите курс"
          value={localFilters["Курс"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Группа">Группа:</label>
        <input
          id="Группа"
          name="Группа"
          placeholder="Введите группу"
          value={localFilters["Группа"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="Факультет">Факультет:</label>
        <input
          id="Факультет"
          name="Факультет"
          placeholder="Введите факультет"
          value={localFilters["Факультет"] || ""}
          onChange={handleChange}
        />
      </div>
      <div className="form-actions">
        <button className="btn btn-submit" type="submit">
          Применить фильтры
        </button>
        <button
          className="btn btn-clear"
          type="button"
          onClick={handleClear}
        >
          Очистить фильтры
        </button>
      </div>
    </form>
  );
}

export default FilterForm;
