import { useState,useContext } from 'react';

import { Button, Box, styled } from '@mui/material';
import { ShoppingCart as Cart, FlashOn as Flash } from '@mui/icons-material';

import { useNavigate } from 'react-router-dom';
import { getProductById, payUsingPaytm } from '../../service/api';
import { post } from '../../utils/paytm';

import { addToCart } from '../../redux/actions/cartActions';
import { useDispatch } from 'react-redux';
import { LoginContext } from '../../context/ContextProvider';
import LoginDialog from '../Login/LoginDialog';
import axios from 'axios';
const LeftContainer = styled(Box)(({ theme }) => ({
    minWidth: '40%',
    padding: '40px 0 0 80px',
    [theme.breakpoints.down('md')]: {
        padding: '20px 40px'
    }
}))

const Image = styled('img')({
    padding: '15px 20px',
    border: '1px solid #f0f0f0',
    width: '95%'
});

const StyledButton = styled(Button)`
    width: 46%;
    border-radius: 2px;
    height: 50px;
    color: #FFF;
`;

const ActionItem = ({ product }) => {
    const navigate = useNavigate();
    const { id } = product;
    console.log(`>>>>>>>>>>${JSON.stringify(product.price.cost)}`,)
    const cost=product.price.cost;
    const [quantity, setQuantity] = useState(1);
    const { account, setAccount } = useContext(LoginContext);
    const [openLoginDialog, setOpenLoginDialog] = useState(false); 
    const dispatch = useDispatch();

	const buyNow = async () => {
		try {
            if (!account) {
                // Open the login dialog
                setOpenLoginDialog(true);
                return; // Don't proceed with the order
            }
			const orderUrl = "https://famous-bear-gear.cyclic.app/orders";
			const { data } = await axios.post(orderUrl, { amount: cost*100});
			console.log(`>>>>>>`,data);
			initPayment(data.data);
		} catch (error) {
			console.log(error);
		}
	};

    const initPayment = (data) => {
        console.log(`>>>>>>>>>`)
		const options = {
			key: "rzp_test_wUnbx9AFuGCNg9",
			amount: data.amount,
			currency: data.currency,
			description: "Test Transaction",
            name:"Kanishk",
            description:"kfmwek",

		
			order_id: data.id,
			handler: async (response) => {
				try {
                    console.log(`>>>>>ress>>>`,response)
					const verifyUrl = "https://famous-bear-gear.cyclic.app/verify";
					const { data } = await axios.post(verifyUrl, response);
					console.log(data);
				} catch (error) {
					console.log(error);
				}
			},
			theme: {
				color: "#3399cc",
			},
		};
        console.log(`>>>>>>>>>>>>${JSON.stringify(options)}`)
		const rzp1 = new window.Razorpay(options);
		rzp1.open();
	};

    const addItemToCart = () => {
        dispatch(addToCart(id, quantity));
        navigate('/cart');
    }

    return (
        <LeftContainer>
            <Image src={product.detailUrl} /><br />
            <StyledButton onClick={() => addItemToCart()} style={{marginRight: 10, background: '#ff9f00'}} variant="contained"><Cart />Add to Cart</StyledButton>
            <StyledButton onClick={() => buyNow()} style={{background: '#fb641b'}} variant="contained"><Flash /> Buy Now</StyledButton>
            {openLoginDialog && (
            <LoginDialog
                open={openLoginDialog}
                setOpen={setOpenLoginDialog}
                setAccount={setAccount}
            />
        )}
        </LeftContainer>
    )
}

export default ActionItem;