import { Container, CssBaseline, makeStyles } from "@material-ui/core";
import React from "react";
import Header from "../Components/Common/header";

const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: "5%",
    // marginLeft: "5%",
  },
}));

export default function Layout({ main }) {
  const classes = useStyles();
  return (
    <div>
      <CssBaseline />
      <Header />
      <Container>
        <div className={classes.root}>{main}</div>
      </Container>
      {/* <Footer /> */}
    </div>
  );
}
