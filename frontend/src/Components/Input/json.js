import { Button, makeStyles } from "@material-ui/core";
import React from "react";

const useStyle = makeStyles((theme) => ({
  root: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    marginTop: "15px",
  },
  div: {
    marginTop: "10px",
  },
}));

export default function UploadJSON(props) {
  const classes = useStyle();

  function onFileChange(e) {
    props.fileUp(e.target.files[0]);
    showFileStatus(e);
  }

  function showFileStatus(e) {
    let div = document.getElementById("file-status");
    div.style.display = "block";
  }

  return (
    <div>
      <Button className={classes.root} variant="contained" component="label">
        Upload JSON
        <input type="file" onChange={onFileChange} accept=".json" hidden />
      </Button>
      <div className={classes.div} id="file-status" style={{ display: "None" }}>
        JSON file upload successful
      </div>
    </div>
  );
}
