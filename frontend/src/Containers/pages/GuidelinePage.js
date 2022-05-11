import {
  Container,
  FormControl,
  InputLabel,
  makeStyles,
  MenuItem,
  Select,
} from "@material-ui/core";
import React, { useState } from "react";
import ReportContainer from "../../Components/Report/reportcontainer";
import { data } from "./GuidelineData";

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(2),
    minWidth: 250,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

function GuidelinePage() {
  const classes = useStyles();

  const [filterKeys, setFilterKeys] = useState({
    0: "",
    1: "",
    2: "",
  });

  const [datas, setDatas] = useState(data);

  const changeHandler = (e) => {
    setFilterKeys({ ...filterKeys, [e.target.name]: e.target.value });
  };

  React.useEffect(() => {
    if (!Object.values(filterKeys).every((value) => !value))
      setDatas(
        data.filter(function (item) {
          for (const key in filterKeys) {
            if (filterKeys[key])
              if (filterKeys[key] !== item.path[key]) {
                return false;
              }
          }
          return true;
        })
      );
  }, [filterKeys]);

  return (
    <Container>
      <center>
        <h1> Guideline Page </h1>
      </center>
      <hr />
      <FormControl className={classes.formControl}>
        <InputLabel>Component</InputLabel>
        <Select
          className={classes.selectEmpty}
          name="0"
          onChange={changeHandler}
        >
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
        <InputLabel>Component Knowledge Aspect</InputLabel>
        <Select
          className={classes.selectEmpty}
          name="1"
          onChange={changeHandler}
        >
          <MenuItem value={"Anatomy"}>Anatomy</MenuItem>
          <MenuItem value={"Behavior"}>Behavior</MenuItem>
          <MenuItem value={"Placement"}>Placement</MenuItem>
          <MenuItem value={"Usage"}>Usage</MenuItem>
        </Select>
      </FormControl>
      <FormControl className={classes.formControl}>
        <InputLabel>Severity of Violations</InputLabel>
        <Select
          className={classes.selectEmpty}
          name="2"
          onChange={changeHandler}
        >
          <MenuItem value={"Permission"}>Permission</MenuItem>
          <MenuItem value={"Error"}>Error</MenuItem>
          <MenuItem value={"Caution"}>Caution</MenuItem>
        </Select>
      </FormControl>

      {datas.map((item, index) => {
        return <ReportContainer data={item} />;
      })}
    </Container>
  );
}

export default GuidelinePage;
