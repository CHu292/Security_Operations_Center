export async function fetchStudents(page, filters) {
    const queryParams = {
      ...filters,
      skip: (page - 1) * 10, 
      limit: 10, 
    };
  
    const queryString = new URLSearchParams(queryParams).toString();
  
    try {
      console.log("Query String:", queryString); 
      const response = await fetch(`http://localhost:3000/students/?${queryString}`);
      console.log("API Response Status:", response.status); 
      if (!response.ok) {
        throw new Error(`API error: ${response.status}`);
      }
  
      const data = await response.json(); 
      console.log("Parsed API Response:", data); 
      return { students: data, total: 100 }; 
    } catch (error) {
      console.error("Error fetching students:", error.message);
      return { students: [], total: 0 }; 
    }
  }
  