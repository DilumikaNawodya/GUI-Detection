import { Button, Grid } from "@material-ui/core";
import React, { useState } from "react";
import UploadImage from "../../Components/Input/Image";
import UploadJSON from "../../Components/Input/json";
import UploadFileService from "../../Services/UploadFileService";
import { useHistory } from "react-router-dom";

export default function Home() {
	const [img, setImg] = useState();
	const [fil, setFile] = useState();
	const history = useHistory()

	const submitForm = () => {
		
		console.log(img)
		console.log(fil)
	
		const formData = new FormData();
		formData.append('image', img);
		formData.append('metajson', fil);

		UploadFileService(formData)
		.then(function(response){
			console.log(response.data)
			localStorage.setItem('imagedata', JSON.stringify(response.data))
			history.push('/image-page')
		})
		.catch(function(error){
			console.log(error)
		})

	}


	return (
		<div>
			<h1>Use Case #1</h1>
			<Grid container spacing={2}>
				<Grid item xs={5} style={{ height: "200px" }}>
					Upload the Mobile Application UI screenshot
					<UploadImage imageUp={setImg} />
				</Grid>
				<Grid item xs={5} style={{ height: "200px" }}>
					Upload the corresponding metadata through a JSON file
					<UploadJSON fileUp={setFile} />
				</Grid>
			</Grid>
			<Button variant="contained" color="primary" onClick={submitForm}>
				Submit
			</Button>
		</div>
	);
}
