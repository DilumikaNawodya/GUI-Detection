import React from "react";
import { BrowserRouter } from "react-router-dom";
import { Switch } from "react-router-dom";
import Layout from "./Containers/layout";
import Home from "./Containers/pages/Home";
import ImagePage from "./Containers/pages/ImagePage";
import ReportPage from "./Containers/pages/ReportPage";
import { allRoutes } from "./routes";

function App() {
	return (
		<div className="App">

			<BrowserRouter>
				<Switch>

					<allRoutes.PublicRoutes exact path="/">
						<Layout main={<Home/>} />
					</allRoutes.PublicRoutes>

					<allRoutes.PublicRoutes exact path="/report-page">
						<Layout main={<ReportPage/>} />
					</allRoutes.PublicRoutes>

					<allRoutes.PublicRoutes exact path="/image-page">
						<Layout main={<ImagePage/>} />
					</allRoutes.PublicRoutes>
				
				</Switch>

			</BrowserRouter>


		</div>
	);
}

export default App;
