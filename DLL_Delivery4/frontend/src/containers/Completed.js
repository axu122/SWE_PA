import React, { Component } from "react";
import Moment from "moment";

// HomePage
import Assesments from "../components/DashboardStudent/Completed";
import axios from "axios";

// Nav
import Nav from "../components/NavBar";

import { Redirect } from "react-router-dom";

const assesmentsCompleted = [
  {
    name: "Delivery 1 Assesments",
    dueDate: Moment(new Date()).subtract(30, "days").calendar(),
    overAll: 3,
    teachersComment: "Do you even code brah?",
  },
  {
    name: "Delivery 2 Assesments",
    dueDate: Moment(new Date()).subtract(20, "days").calendar(),
    overAll: 3,
    teachersComment: "When are you dropping?",
  },
  {
    name: "Delivery 3 Assesments",
    dueDate: Moment(new Date()).subtract(15, "days").calendar(),
    overAll: 3,
    teachersComment: "Thoughts on millitary school?",
  },
  {
    name: "Delivery 4 Assesments",
    dueDate: Moment(new Date()).subtract(5, "days").calendar(),
    overAll: 2,
    teachersComment: "You gucci?",
  },
];

class StudentHome extends Component {
  state = {
    logout: false,
    changePassword: false,
  };
  changePassword = () => {
    console.log("changepwd");
    this.setState({
      changePassword: true,
    });
  };

  onLogout = () => {
    console.log("here");
    this.setState({
      logout: true,
    });
  };
  render() {
    //write a get request to get all assessments!!!!!
    //Http Request
    console.log("Load Student Completed Assessments");

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

    console.log("View Student Completed Assessments");
    //Using axios to write post request to Django server that is handled in requestHandler.py to validate
    axios
      .post(
        "/studentcompletedassessments/",
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
        <Assesments completedArr={assesmentsCompleted} />
        {this.state.changePassword === true ? (
          <Redirect to="/changepassword" />
        ) : null}
        {this.state.logout === true ? <Redirect to="/login" /> : null}
      </Nav>
    );
  }
}

export default StudentHome;
