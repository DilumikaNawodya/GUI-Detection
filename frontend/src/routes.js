import React from 'react';
import { Route } from 'react-router-dom';

export const allRoutes = {
    PublicRoutes,
}


function PublicRoutes(props){
    const { component: Component, ...rest } = props
    return (
        <div>
            <Route
                {...rest}
                render={props => (
                    <Component {...props} />
                )}
            />
        </div>
    )
}