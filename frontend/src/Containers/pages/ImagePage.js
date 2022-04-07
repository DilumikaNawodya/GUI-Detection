import React, { useEffect, useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";

import {
	Button,
	Card,
	Container,
	Divider,
	FormControl,
	InputLabel,
	MenuItem,
	Select,
	Typography,
	useTheme,
} from "@material-ui/core";
import EventAvailableOutlinedIcon from "@material-ui/icons/EventAvailableOutlined";
import GetComponentItem from "../../Services/getComponentItem";
import { useHistory } from "react-router-dom";


const useStyles = makeStyles((theme) => ({
	root: {
		margin: theme.spacing(1),
	},
	paper: {
		padding: theme.spacing(2),
		textAlign: "center",
	},
	formControl: {
		margin: theme.spacing(5),
		minWidth: 150,
		maxWidth: 300,
	},
	button: {
		margin: theme.spacing(5),
		minWidth: 150,
		maxWidth: 300,
	},
	chips: {
		display: "flex",
		flexWrap: "wrap",
		minWidth: 150,
	},
	chip: {
		margin: 5,
	},
	noLabel: {
		marginTop: theme.spacing(3),
	},
	card: {
		marginTop: theme.spacing(2),
		padding: theme.spacing(2),
	},
	cardgrid: {
		margin: theme.spacing(1),
		padding: theme.spacing(1),
	},
	paperTodo: {
		margin: theme.spacing(1),
		padding: theme.spacing(2),
	},
}));


export default function ImagePage() {

	const imagedata = JSON.parse(localStorage.getItem('imagedata'))
	const history = useHistory()
	const classes = useStyles();
	const eleCount = [];

	for (let i = 0; i <= imagedata.no_of_compos; i++) {
		eleCount[i] = i;
	}


	const [formValue, setFormValue] = React.useState({
		element: [],
		component: [],
	});

	const [finalList, setfinalList] = useState([]);

	const handleSubmit = (e) => {
		e.preventDefault();
		setfinalList([...finalList, formValue]);
	};

	const handleChange = (event) => {
		setFormValue({
			...formValue,
			[event.target.name]: event.target.value,
		});
	};

	const addedListSubmit = () => {
		GetComponentItem(finalList, imagedata.json_name)
		.then(function(response){
			console.log(response.data)
			history.push('/report-page')
		})
		.catch(function(error){
			console.log(error)
		})
	};


	return (
		<div className={classes.root}>
			<Container>
				<Typography>
					<center>
						<h1>Image Details</h1>
					</center>
				</Typography>
				<Divider style={{ marginBottom: "15px" }} />
				<Grid container spacing={2}>
					<Grid item xs={6}>
						<Typography class={classes.root}>
							<h2>Detected Image</h2>
						</Typography>
						<img src={imagedata.combinedimage.url} alt="icons" width="500" />
						<Divider orientation="vertical" flexItem />
					</Grid>
					<Grid item xs={6} >
						<Card>
							<Typography className={classes.button}>
								<Grid container spacing={2}>
									<Grid item xs={2}>
										<EventAvailableOutlinedIcon style={{ fontSize: 40 }} />
									</Grid>
									<Grid item xs={10}>
										<h2>Options Available</h2>
									</Grid>
								</Grid>
							</Typography>
							<form onSubmit={handleSubmit}>
								<FormControl variant="outlined" className={classes.formControl}>
									<InputLabel id="demo-simple-select-outlined-label">
										Element
									</InputLabel>
									<Select
										labelId="demo-simple-select-outlined-label"
										id="demo-simple-select-outlined"
										value={formValue.element}
										onChange={handleChange}
										label="Element"
										name="element"
										required
									>
										{eleCount.map((e, index) => {
											return (
												<MenuItem value={e}>{e}</MenuItem>
											);
										})}

									</Select>
								</FormControl>
								<FormControl variant="outlined" className={classes.formControl}>
									<InputLabel id="demo-simple-select-outlined-label">
										Component
									</InputLabel>
									<Select
										labelId="demo-simple-select-outlined-label"
										id="demo-simple-select-outlined"
										value={formValue.component}
										onChange={handleChange}
										label="Component"
										name="component"
										required
									>
										<MenuItem value={"App Bar - Bottom"}>
											App Bar - Bottom
										</MenuItem>
										<MenuItem value={"App Bar - Top"}>App Bar - Top</MenuItem>
										<MenuItem value={"Bottom Navigation"}>
											Bottom Navigation
										</MenuItem>
										<MenuItem value={"Navigation Drawer"}>
											Navigation Drawer
										</MenuItem>
										<MenuItem value={"Buttons Buttons - FAB"}>
											Buttons Buttons - FAB
										</MenuItem>
										<MenuItem value={"Lists"}>Lists</MenuItem>
										<MenuItem value={"Cards"}>Cards</MenuItem>
										<MenuItem value={"Text fields"}>Text fields</MenuItem>
										<MenuItem value={"Tabs"}>Tabs</MenuItem>
										<MenuItem value={"Dialogs"}>Dialogs</MenuItem>
										<MenuItem value={"Banner"}>Banner</MenuItem>
									</Select>
								</FormControl>

								<br />
								<Divider />
								<Button
									type="submit"
									variant="contained"
									color="primary"
									className={classes.button}
								>
									Add
								</Button>
							</form>
						</Card>
						<Card className={classes.card}>
							<Grid container spacing={2}>
								<Grid item xs={10}>
									<Typography>
										<h3>Added Elements and Components</h3>
									</Typography>
								</Grid>
								<Grid item xs={2}>
									<Button
										type="submit"
										variant="contained"
										color="primary"
										onClick={addedListSubmit}
										style={{ background: "#4caf50" }}
									>
										Submit
									</Button>
								</Grid>
							</Grid>
							<Divider />
							<Grid container spacing={2}>
								{finalList &&
									finalList.map((e, index) => {
										return (
											<div key={index}>
												<Grid item xs className={classes.cardgrid}>
													<Paper
														className={classes.paperTodo}
														style={{ color: "#fafafa", background: "#616161" }}
													>
														Element {e.element} <b>|</b> {e.component}
													</Paper>
												</Grid>
											</div>
										);
									})}
							</Grid>
						</Card>
					</Grid>
				</Grid>

			</Container>
		</div>
	);
}
