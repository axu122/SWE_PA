import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import PeopleIcon from '@material-ui/icons/People';
import BarChartIcon from '@material-ui/icons/BarChart';
import LayersIcon from '@material-ui/icons/Layers';
import LibraryBooksIcon from '@material-ui/icons/LibraryBooks';
import { Link} from 'react-router-dom';


export const mainListItems = (
  <div>
    <ListItem button component={Link} to={'/studentHome'}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Home" />
    </ListItem>

    <ListItem button component={Link} to={'/studentHome/assessments'}>
      <ListItemIcon>
        <BarChartIcon />
      </ListItemIcon>
      <ListItemText primary="Peer Assessments" />
    </ListItem>

    <ListItem button component={Link} to={'/studentHome/completed'}>
      <ListItemIcon>
        <LayersIcon />
      </ListItemIcon>
      <ListItemText primary="Results" />
    </ListItem>
  </div>
);

export const secondaryListItems = (
  <div>
    <ListItem button component={Link} to={'/professorHome'}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Home" />
    </ListItem>

    <ListItem button component={Link} to={'/professorHome/assessments'}>
      <ListItemIcon>
        <BarChartIcon />
      </ListItemIcon>
      <ListItemText primary="Class Assessments" />
    </ListItem>

    <ListItem button component={Link} to={'/professorHome/teams'}>
      <ListItemIcon>
        <PeopleIcon/>
      </ListItemIcon>
      <ListItemText primary="Teams & Students" />
    </ListItem>
    <ListItem button component={Link} to={'/professorHome/questions'}>
      <ListItemIcon>
        <LibraryBooksIcon/>
      </ListItemIcon>
      <ListItemText primary="Questions" />
    </ListItem>

    
  </div>
);
//Add onclick property to the button
export const tertiaryListItems = (
  <div>
    <ListItem button component={Link} to={'/professorHome'}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Home" />
    </ListItem>
  </div>
);

//Add onclick property to the button
export const fourthListItems = (
  <div>
    <ListItem button component={Link} to={'/studentHome'}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Home" />
    </ListItem>
  </div>
);