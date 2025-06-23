export async function fetchStudents(page, filters) {
    const queryParams = {
      ...filters,
      skip: (page - 1) * 10, // Lấy dữ liệu từ vị trí này
      limit: 10, // Số lượng bản ghi mỗi trang
    };
  
    const queryString = new URLSearchParams(queryParams).toString();
  
    try {
      console.log("Query String:", queryString); // Debug query string
      const response = await fetch(`http://localhost:3000/students/?${queryString}`);
      console.log("API Response Status:", response.status); // Debug trạng thái HTTP
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
  
      const data = await response.json(); // Parse JSON từ phản hồi
      console.log("Parsed API Response:", data); // Debug dữ liệu từ API
      return { students: data, total: 100 }; // Giả định tổng số là 100
    } catch (error) {
      console.error("Error fetching students:", error.message);
      return { students: [], total: 0 }; // Trả về dữ liệu mặc định nếu lỗi
    }
  }
  