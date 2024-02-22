import React from 'react';

import { StyledEngineProvider, Theme } from '@mui/material/styles'
import { CssBaseline } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";

const TemplateContext = React.createContext(null);

export const TemplateProvider = ({ children }) => {
    const theme = createTheme();

    return (
        <TemplateContext.Provider value={{}}>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                {children}
            </ThemeProvider>
        </TemplateContext.Provider>
    );
}

export default TemplateProvider;