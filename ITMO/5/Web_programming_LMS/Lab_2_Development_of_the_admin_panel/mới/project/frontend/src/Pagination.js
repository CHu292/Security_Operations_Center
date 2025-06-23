import React from "react";
import "./styles/main.css"; // Import CSS

function Pagination({ currentPage, setPage, totalPages }) {
  const handlePrevious = () => {
    if (currentPage > 1) {
      setPage(currentPage - 1);
    }
  };

  const handleNext = () => {
    if (currentPage < totalPages) {
      setPage(currentPage + 1);
    }
  };

  return (
    <div className="pagination">
      <button
        className="pagination-button"
        disabled={currentPage === 1}
        onClick={handlePrevious}
      >
        &laquo; Previous
      </button>
      <span className="pagination-info">
        Trang {currentPage} trên {totalPages}
      </span>
      {Array.from({ length: totalPages }, (_, i) => (
        <button
          key={i}
          className={`pagination-button ${
            currentPage === i + 1 ? "active" : ""
          }`}
          onClick={() => setPage(i + 1)}
        >
          {i + 1}
        </button>
      ))}
      <button
        className="pagination-button"
        disabled={currentPage === totalPages}
        onClick={handleNext}
      >
        Next &raquo;
      </button>
    </div>
  );
}

export default Pagination;
