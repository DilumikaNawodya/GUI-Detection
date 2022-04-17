import React from "react";
import { Button, makeStyles } from "@material-ui/core";
import { AppBar } from "@material-ui/core";
import { Toolbar } from "@material-ui/core";
import { Typography } from "@material-ui/core";
import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
  high: {
    fontWeight: "900",
  },
  low: {
    fontWeight: "100",
  },
  headerColor: {
    backgroundColor: "#28282B",
  },
}));

export default function Header() {
  const classes = useStyles();
  const history = useHistory();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.headerColor}>
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Createaro
          </Typography>
          <Button
            color="inherit"
            onClick={() => {
              history.push("/guideline-page");
            }}
          >
            Guidelines
          </Button>
          <Button
            color="inherit"
            onClick={() => {
              history.push("/");
            }}
          >
            Detect
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}
