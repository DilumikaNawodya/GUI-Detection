import {
  Container,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Button,
} from "@material-ui/core";
import { makeStyles } from "@material-ui/core";
import React, { useState } from "react";
import ReportContainer from "../../Components/Report/reportcontainer";
import SearchIcon from "@material-ui/icons/Search";
import { data } from "./GuidelineData";

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(2),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
  button: {
    marginTop: theme.spacing(3.5),
  },
}));

function GuidelinePage() {
  const classes = useStyles();
  const datas = data;

  const [filters, setFilters] = useState({});

  const updateFilters = (searchparams) => {
    setFilters(searchparams);
  };

  return (
    <Container>
      <center>
        <h1> Guideline Page </h1>
      </center>
      <hr />
      <FormControl className={classes.formControl}>
        <InputLabel>Component</InputLabel>
        <Select className={classes.selectEmpty}>
          <MenuItem value={"Appbar: Bottom"}>Appbar: Bottom</MenuItem>
          <MenuItem value={"Appbar: Top"}>Appbar: Top</MenuItem>
          <MenuItem value={"Bottom Navigation"}>Bottom Navigation</MenuItem>
          <MenuItem value={"Navigation Drawer"}>Navigation Drawer</MenuItem>
          <MenuItem value={"Button"}>Button</MenuItem>
          <MenuItem value={"Floating Action Button"}>
            Floating Action Button
          </MenuItem>
          <MenuItem value={"Lists"}>Lists</MenuItem>
          <MenuItem value={"Cards"}>Cards</MenuItem>
          <MenuItem value={"Text fields"}>Text fields</MenuItem>
          <MenuItem value={"Tabs"}>Tabs</MenuItem>
          <MenuItem value={"Dialogs"}>Dialogs</MenuItem>
          <MenuItem value={"Banner"}>Banner</MenuItem>
        </Select>
      </FormControl>
      <FormControl className={classes.formControl}>
        <InputLabel>CKA</InputLabel>
        <Select className={classes.selectEmpty}>
          <MenuItem value={"Anatomy"}>Anatomy</MenuItem>
          <MenuItem value={"Behavior"}>Behavior</MenuItem>
          <MenuItem value={"Placement"}>Placement</MenuItem>
          <MenuItem value={"Usage"}>Usage</MenuItem>
        </Select>
      </FormControl>
      <FormControl className={classes.formControl}>
        <InputLabel>Severity</InputLabel>
        <Select className={classes.selectEmpty}>
          <MenuItem value={"Permission"}>Permission</MenuItem>
          <MenuItem value={"Error"}>Error</MenuItem>
          <MenuItem value={"Caution"}>Caution</MenuItem>
        </Select>
      </FormControl>
      <Button
        type="submit"
        variant="contained"
        color="primary"
        className={classes.button}
      >
        <SearchIcon />
      </Button>

      {datas.map((item, index) => {
        return <ReportContainer data={item} />;
      })}
    </Container>
  );
}

export default GuidelinePage;
