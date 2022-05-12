import { Button, makeStyles } from "@material-ui/core";
import React from "react";
// import UploadFileService from "../../Services/ImageServices/uploadFileService";

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

export default function UploadImage(props) {
  const classes = useStyle();

  function onImageChange(e) {
    props.imageUp(e.target.files[0]);
    showImageStatus(e);
  }

  function showImageStatus(e) {
    let div = document.getElementById("image-status");
    div.style.display = "block";
  }

  return (
    <div>
      <Button className={classes.root} variant="contained" component="label">
        Upload image
        <input type="file" onChange={onImageChange} accept="image/*" hidden />
      </Button>
      <div
        className={classes.div}
        id="image-status"
        style={{ display: "None" }}
      >
        Image upload successful
      </div>
    </div>
  );
}
