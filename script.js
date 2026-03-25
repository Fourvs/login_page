async function uploadResume() {
  const input = document.getElementById("resume");

  input.click();

  input.onchange = async () => {
    const file = input.files[0];
    document.getElementById("fileName").innerText = file.name;

    const formData = new FormData();
    formData.append("resume", file);

    const response = await fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    localStorage.setItem("result", JSON.stringify(data));
    window.location.href = "dashboard.html";
  };
}
