async function getData() {
    let data;

    try {
        const response = await fetch("http://127.0.0.1:5000/students");
        data = await response.json();
    } catch (error) {
        console.error('Xato:', error);
    }

    return data;
}
let container = document.querySelector(".container");

getData().then(data => {
    for (const [course, students] of Object.entries(data)) {
        let dataTitle = document.createElement("div");
        dataTitle.className = "data_title";
        dataTitle.textContent = course;

        let showData = document.createElement("div");
        showData.className = "data_wrapper";
        main_data_wapper = document.createElement('div');
        main_data_wapper.className = "main_data_wrapper"
        showData.append(dataTitle);
        showData.append(main_data_wapper)
        for (const [studentId, studentInfo] of Object.entries(students)) {
            let dataInfo = document.createElement("div");
            dataInfo.className = "main_data";

            let studentIdElem = document.createElement("p");
            studentIdElem.textContent = `ID: ${studentId}`;
            dataInfo.append(studentIdElem);

            for (const [key, value] of Object.entries(studentInfo)) {
                let studentDetail = document.createElement("p");
                studentDetail.textContent = `${key}: ${value}`;
                dataInfo.append(studentDetail);
            }

            main_data_wapper.append(dataInfo);
        }

        container.append(showData);
    }
});
