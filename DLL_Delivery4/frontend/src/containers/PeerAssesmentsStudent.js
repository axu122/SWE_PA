import React, { Component } from "react";
import Moment from "moment";

// HomePage
import Assesments from "../components/DashboardStudent/Assesments";
import ToDOModal from "../components/DashboardStudent/SubmitModal";
import axios from "axios";

// Nav
import Nav from "../components/NavBar";

// redirect
import { Redirect } from "react-router-dom";

const assesmentsToDo = [
  {
    name: "Delivery 6 Assesments",
    teamMates: ["Pedro", "John", "Adam"],
    dueDate: new Date(),
    id: 12312,
  },
];

const assesmentsClosed = [
  {
    name: "Delivery 5 Assesments",
    teamMates: ["Pedro", "John", "Adam"],
    dueDate: Moment(new Date()).subtract(10, "days").calendar(),
    id: 12312,
  },
];

class StudentHome extends Component {
  state = {
    openToDoModal: false,
    todoSelected: null,
    toDoIndex: null,
    todoResponses: null,
    logout: false,
    changePassword: false,
    disableSubmit: false,
    assesmentsToDo: assesmentsToDo,
  };

  // *----------HANDLE MODAL METHODS------------------*
  openModalHandler = (e) => {
    console.log(assesmentsToDo[e]);
    console.log(e);
    this.setState({
      openToDoModal: true,
      todoSelected: assesmentsToDo[e],
      toDoIndex: e,
    });
  };

  handleClose = () => {
    this.setState({
      openToDoModal: false,
    });
  };

  //  *------------Submit ToDo Functions -------------*
  submitGradeHandler = () => {
    //Http Request
    console.log("Submit student assessment Modal");

    //--------------------------------------------------------------------
    //function to get the cookie from req in order to handle the csrf token
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    //get csrf token in order to not have request blocked
    var csrftoken = getCookie("csrftoken");
    //--------------------------------------------------------------------

    console.log("Student Grade Modal request");
    console.log("this.state.toDoIndex: " + this.state.toDoIndex);
    console.log("this.state.todoSelected: " + this.state.todoSelected);
    //Using axios to write post request to Django server that is handled in requestHandler.py to validate
    axios
      .post(
        "/studentgrade/",
        {
          toDoIndex: this.state.toDoIndex,
          todoSelected: this.state.todoSelected,
          email: localStorage.getItem("userEmail"),
          type: localStorage.getItem("userType"),
        },
        {
          headers: {
            "X-CSRFToken": csrftoken,
          },
        }
      )
      .then(
        (response) => {
          var data = response.data;
          console.log(response.data);
        },
        (error) => {
          console.log(error);
        }
      );
    assesmentsToDo.splice(this.state.toDoIndex, 1);

    this.setState({
      openToDoModal: false,
      toDoIndex: null,
      todoSelected: null,
    });
  };

  changePassword = () => {
    console.log("changepwd");
    this.setState({
      changePassword: true,
    });
  };

  // LOGOUT
  onLogout = () => {
    console.log("here");
    this.setState({
      logout: true,
    });
  };

  render() {
    //write a get request to get all assessments!!!!!
    //Http Request
    console.log("Load Student Peer Assessments");

    //--------------------------------------------------------------------
    //function to get the cookie from req in order to handle the csrf token
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === name + "=") {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    //get csrf token in order to not have request blocked
    var csrftoken = getCookie("csrftoken");
    //--------------------------------------------------------------------

    console.log("View Student Peer Assessments");
    //Using axios to write post request to Django server that is handled in requestHandler.py to validate
    axios
      .post(
        "/studentpeerassessments/",
        {
          email: localStorage.getItem("userEmail"),
          type: localStorage.getItem("userType"),
        },
        {
          headers: {
            "X-CSRFToken": csrftoken,
          },
        }
      )
      .then(
        (response) => {
          var data = response.data;
          console.log("responded to get request");
          console.log(response.data);
        },
        (error) => {
          console.log(error);
        }
      );
    //--------------------------------------------------------------------

    return (
      <Nav
        user="Student"
        onLogout={this.onLogout}
        changePassword={this.changePassword}
      >
        <Assesments
          toDoArr={assesmentsToDo}
          closedArr={assesmentsClosed}
          openModal={this.openModalHandler}
        />

        <ToDOModal
          close={this.handleClose}
          open={this.state.openToDoModal}
          info={this.state.todoSelected}
          submit={this.submitGradeHandler}
          disable={this.state.disableSubmit}
          //onChangeHandler={} For when stuff is typed into comments
        />
        {this.state.changePassword === true ? (
          <Redirect to="/changepassword" />
        ) : null}
        {this.state.logout === true ? <Redirect to="/login" /> : null}
      </Nav>
    );
  }
}

export default StudentHome;
