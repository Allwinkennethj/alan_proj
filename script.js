const hamburger = document.querySelector(".hamburger");
const navbar = document.querySelector("ul");
hamburger.addEventListener("click", () => {
  navbar.classList.toggle("slide");
});

const localemail = localStorage.getItem("email");
const localname = localStorage.getItem("name");
const localdesig = localStorage.getItem("desig");
const localage = localStorage.getItem("age");

localemail ? (document.getElementById("localemail").value = localemail) : null;

localname ? (document.getElementById("localname").value = localname) : null;

localdesig ? (document.getElementById("localdesig").value = localdesig) : null;

localage ? (document.getElementById("localage").value = localage) : null;

function login() {
  var creds = {
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
  };
  fetch("http://localhost:5000/user/login", {
    method: "POST",
    body: JSON.stringify(creds),
    headers: {
      "Content-type": "application/json",
    },
  }).then((res) => {
    res.json().then((data) => {
      console.log(data);
      if (data.status_code === 200) {
        if (creds.email === "admin") {
          window.location.href = "./index.html";
        } else {
          localStorage.setItem("email", data.data.email);
          localStorage.setItem("name", data.data.name);
          localStorage.setItem("desig", data.data.designation);
          localStorage.setItem("age", data.data.age);
          window.location.href = "./evaluation.html";
        }
      }
    });
  });
}

const getUsers = () => {
  fetch("http://localhost:5000/user/getall", {
    method: "GET",
    headers: {
      "Content-type": "application/json",
    },
  })
    .then((res) => {
      res.json().then((data) => {
        console.log(data.message);

        if (data.message.length > 0) {
          var temp = "";
          data.message.forEach((itemData) => {
            temp += "<tr>";
            temp += "<td>" + itemData.email + "</td>";
            temp += "<td>" + itemData.name + "</td>";
            temp += "<td>" + itemData.designation + "</td>";
            temp += "<td>" + itemData.age + "</td>";
            temp += "</tr>";
          });
          document.querySelector(".tableBody").innerHTML = temp;
        }
      });
    })
    .catch((error) => {
      console.error(error);
    });
};

const signup = () => {
  var data = {
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
  };

  fetch("http://localhost:5000/user/adduser", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((res) => {
      res.json().then((data) => {
        if (data.status_code === 200) {
          window.location.href = "./login.html";
        }
      });
    })
    .catch((error) => {
      console.error(error);
    });
};

const evaluation = (e) => {
  e.preventDefault();
  var data = {
    email: document.getElementById("localemail").value,
    name: document.getElementById("localname").value,
    designation: document.getElementById("localdesig").value,
    age: document.getElementById("localage").value,
  };
  fetch("http://localhost:5000/user/edit", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify(data),
  }).then((res) => {
    res.json().then((data) => {
      if (data.status_code === 200) {
        localStorage.setItem("email", data.data.email);
        localStorage.setItem("name", data.data.name);
        localStorage.setItem("desig", data.data.designation);
        localStorage.setItem("age", data.data.age);
        window.location.reload();
      }
    });
  });
};

const logout = () => {
  localStorage.clear();
  window.location.href = "./login.html";
};
