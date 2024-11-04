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
let container = document.querySelector(".student_info_wrapper");

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



function add_student(student_data) {
    const apiUrl = "http://192.168.0.102:5000/add_student";
    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(student_data)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Talabani qo'shishda xatolik yuz berdi");
            }
            return response.json();
        })
        .then(data => {
            console.log("Javob:", data);
        })
        .catch(error => {
            console.error("Xatolik:", error);
        });
}

function show_info(name, age, id, course, gender, city, region, street, house) {
    const sorted_data = {
        name: name.value,
        age: age.value,
        id: id.value,
        course: course.value.toLowerCase(),
        gender: gender.value.toLowerCase(),
        city: city.value,
        region: region.value,
        street: street.value,
        house: house.value
    };

    if (Object.values(sorted_data).every(value => value !== "")) {
        add_student(sorted_data);
    }else{
        alert("fill out the form first")
    }
}
let tabs_induc = false

function change_tabs(elem_1 , elem_2, elem){
    if(tabs_induc){
        elem_1.style.cssText = "display:none"
        elem_2.style.cssText = "display:block"
        elem.textContent = "Add Student"
        tabs_induc = false
    } else {
        elem_1.style.cssText = "display:block"
        elem_2.style.cssText = "display:none"
        elem.textContent = "Students List"
        tabs_induc = true
    }
}