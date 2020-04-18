import React, {Component} from 'react'
import Moment from 'moment'

// HomePage
import Assesments from '../components/DashboardProfessor/AllAssesments'
import ToDOModal from '../components/DashboardProfessor/ModalProfessor'
import CreateModal from '../components/DashboardProfessor/CreateModal'
import axios from 'axios'


// Nav
import Nav from '../components/NavBar'
import SnackBar from '../components/Login/SnackBar'


// redirect
import {Redirect} from 'react-router-dom'

//List of assessments for prof to grade??
const toGrade=[
    {
        name:'Pedro',
        team:1,
        overallGrade:3.5,
        assessment:'Delivery 5 Assessments'
    },
    {
        name:'John',
        team:4,
        overallGrade:4.5,
        assessment:'Delivery 5 Assessments'
    },
    {
        name:'Adam',
        team:2,
        overallGrade:3.9,
        assessment:'Delivery 5 Assessments'
    }
]
//List of all assessments
const allAssesments=[
    {
        name:'Delivery 1 Assessments',
        dueDate:  Moment(new Date()).subtract(30, 'days').calendar(),
        overAll: 4.3,
    },
    {
        name:'Delivery 2 Assessments',
        dueDate:  Moment(new Date()).subtract(20, 'days').calendar(),
        overAll: 4.2,
    },
    {
        name:'Delivery 3 Assessments',
        dueDate:  Moment(new Date()).subtract(15, 'days').calendar(),
        overAll: 3.3,
    },
    {
        name:'Delivery 4 Assessments',
        dueDate:  Moment(new Date()).subtract(12, 'days').calendar(),
        overAll: 2.7,
    },
]



class StudentHome extends Component{

    state={
        openToDoModal:false,
        todoSelected:null,
        toDoIndex:null,
        todoResponses:null,
        logout:false,
        createModal:false,
        changePassword:false,
        assessmentName: null,
        assesmentDueDate:null,
        notification:false,

        toGrade:toGrade

    }


    // *----------HANDLE MODAL METHODS------------------*
     openModalHandler = (e) => {

        this.setState({
            openToDoModal:true,
            todoSelected:toGrade[e],
            toDoIndex:e

        });
      };
    
    handleClose = () => {
        this.setState({
            openToDoModal:false,
            createModal:false
        })
      };

      openCreateModal = () => {
       console.log("Open Modal for making assessment")
       this.setState({
        createModal:true,

       });
     };


    // *------------ HANDLE CHANGE TEXT ----------------*
    textHandler=e=>{
        this.setState({
            [e.target.id]:e.target.value
        })
    }

    //  *------------Assesment Create Functions -------------*
    submitNewHandler=()=>{
        //adds assessment to all assessments

        //Http Request
        console.log("Add Assessment")

        //--------------------------------------------------------------------
        //function to get the cookie from req in order to handle the csrf token
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        //get csrf token in order to not have request blocked
        var csrftoken = getCookie('csrftoken');
        //--------------------------------------------------------------------

        console.log("Add assessment request")
        //Using axios to write post request to Django server that is handled in requestHandler.py to validate
        axios.post('/addassessmentreq/',{
            name:this.state.assessmentName,
            dueDate:this.state.assesmentDueDate,
            overAll:'0',
            email: localStorage.getItem('userEmail'),
            type: localStorage.getItem('userType')
        },
        {
            headers: {
                'X-CSRFToken': csrftoken
            }
        }).then((response) => {
              var data = response.data
              console.log(response.data);
        }, (error) => {
          console.log(error);
        });


        allAssesments.push({
            name:this.state.assessmentName,
            dueDate:this.state.assesmentDueDate,
            overAll:'0'
        })

        this.setState({
            assessmentName:null,
            assesmentDueDate:null,
            createModal:false,
            notification:true
        })
    }

      //  *------------Submit ToDo Functions -------------*
      submitToDoHandler=()=>{
        //Http Request
        console.log("Submit Todo Modal")

        //--------------------------------------------------------------------
        //function to get the cookie from req in order to handle the csrf token
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        //get csrf token in order to not have request blocked
        var csrftoken = getCookie('csrftoken');
        //--------------------------------------------------------------------

        console.log("To Grade Modal request")
        console.log("this.state.toDoIndex: " + this.state.toDoIndex)
        console.log("this.state.todoSelected: " + this.state.todoSelected)
        //Using axios to write post request to Django server that is handled in requestHandler.py to validate
        axios.post('/professorgrade/',{
            toDoIndex:this.state.toDoIndex,
            todoSelected:this.state.todoSelected,
            email: localStorage.getItem('userEmail'),
            type: localStorage.getItem('userType')
        },
        {
            headers: {
                'X-CSRFToken': csrftoken
            }
        }).then((response) => {
              var data = response.data
              console.log(response.data);
        }, (error) => {
          console.log(error);
        });
       toGrade.splice(this.state.toDoIndex,1)


       this.setState({
            openToDoModal:false,
            createModal:false,
            toDoIndex:null,
            todoSelected:null
        })
    }

    //  *------------ CLOSE NOTIFICATION ----------------*
    handleCloseNot = (event, reason) => {
        if (reason === 'clickaway') {
          return;
        }
    
        this.setState({
            notification:false
        })
      };

    changePassword=()=>{
        console.log('changepwd')
        this.setState({
            changePassword:true
        })
    };

    // LOGOUT
      onLogout=()=>{
        console.log('here')
        this.setState({
            logout:true
        })
    }



    render(){

      //write a get request to get all assessments!!!!!
        //Http Request
        console.log("Load assessments")

        //--------------------------------------------------------------------
        //function to get the cookie from req in order to handle the csrf token
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        //get csrf token in order to not have request blocked
        var csrftoken = getCookie('csrftoken');
        //--------------------------------------------------------------------

        console.log("View assessments page")
        //Using axios to write post request to Django server that is handled in requestHandler.py to validate
        axios.get('/assessmentview/',{
            email: localStorage.getItem('userEmail'),
            type: localStorage.getItem('userType')
        },
        {
            headers: {
                'X-CSRFToken': csrftoken
            }
        }).then((response) => {
              var data = response.data
              console.log("responded to get request");
              console.log(response.data);
        }, (error) => {
          console.log(error);
        });
        //--------------------------------------------------------------------

        return(
            <Nav
                user="Professor"
                onLogout={this.onLogout}
                changePassword={this.changePassword}
            >
                <Assesments
                toGrade={toGrade}
                closedArr={allAssesments}
                openModal={this.openModalHandler}
                openCreate={this.openCreateModal}
                />

            <ToDOModal 
                close={this.handleClose}
                open={this.state.openToDoModal}
                info={this.state.todoSelected}
                submit={this.submitToDoHandler}
            />

            <CreateModal 
                close={this.handleClose}
                open={this.state.createModal}
                onChangeHandler={this.textHandler}
                assessmentName={this.state.assessmentName}
                assessmentDate={this.state.assesmentDueDate}
                submit={this.submitNewHandler}
                type='assessment'

            />

            <SnackBar 
                    message='Assesment Created'
                    open={this.state.notification}
                    handleClose={this.handleCloseNot}
                
                />
            {this.state.changePassword===true?<Redirect to='/changepassword' />:null}
            {this.state.logout===true?<Redirect to='/login' />:null}

            </Nav>
        )
    }
}

export default StudentHome