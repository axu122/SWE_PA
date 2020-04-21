import React, {Component} from 'react'
import {Redirect} from 'react-router-dom'

// HomePage
import HomePage from '../components/DashboardProfessor/ProfessorHome'
import axios from 'axios'


// Nav
import Nav from '../components/NavBar'



//List of assessments for prof to grade??
const classes=[
    {
        name:'Software Engineering',
        teams:3
    },
    {
        name:'Computer Science 1',
        teams:4
    },
    {
        name:'Computer Science 2',
        teams:15
    }
]

class ProfessorHome extends Component{
    state={
        logout:false,
        changePassword:false,
        selectedClass:false,
        selected:null,
        selectedIndex:null,
        class:null
    }

    selectClassHandler = (e) => {
        //add to local storage the class selected
        localStorage.setItem('selectedClass', e.name)
        this.setState({
            selectedClass:true,
            selected:classes[e],
            selectedIndex:e

        });
      };


    changePassword=()=>{
        console.log('changepwd')
        this.setState({
            changePassword:true
        })
    };
    onLogout=()=>{
        console.log('here')
        this.setState({
            logout:true
        })
    }

    render(){
         //write a get request to get all assessments!!!!!
        //Http Request
        console.log("Load prof homepage")

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

        console.log("View prof homepage")
        //Using axios to write post request to Django server that is handled in requestHandler.py to validate
        axios.get('/professorhomepage/',{
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
//        if(localStorage.getItem('selectedClass')!=null){
//            this.setState({
//                user:false
//            })
//        }
        return(
            <Nav
                user='ProfessorHome'
                changePassword={this.changePassword}
                onLogout={this.onLogout}
            >
                <HomePage
                    classes={classes}
                    selectClass={this.selectClassHandler}
                />
            {this.state.selectedClass===true?<Redirect to='/professorHome/assessments' />:null}
            {this.state.changePassword===true?<Redirect to='/changepassword' />:null}
            {this.state.logout===true?<Redirect to='/login' />:null}

            </Nav>
        )
    }
}

export default ProfessorHome