import React, { useState } from "react";

import { ButtonGroup, Button, styled } from "@mui/material";

const Component = styled(ButtonGroup)`
    margin-top: 30px;
`;

const StyledButton = styled(Button)`
    border-radius: 50%;
`;

const GroupedButton = () => {
    const [ counter, setCounter ] = useState(1);

    const handleIncrement = () => {
        setCounter(counter => counter + 1 );
    };

    const handleDecrement = () => {
        setCounter(counter => counter - 1 );
    };

    return (
        <Component>
            <StyledButton onClick={() => handleDecrement()} disabled={counter == 0}>-</StyledButton>
            <Button disabled>{counter}</Button>
            <StyledButton onClick={() => handleIncrement()}>+</StyledButton>
        </Component>
    );
}

export default GroupedButton;