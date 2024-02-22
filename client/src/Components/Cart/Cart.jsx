import { useEffect,useState,state } from 'react';

import { Box, Typography, Button, Grid, styled } from '@mui/material';
import { useParams } from 'react-router-dom';

import { useSelector, useDispatch } from 'react-redux';
import { addToCart, removeFromCart } from '../../redux/actions/cartActions';

import TotalView from './TotalView';
import EmptyCart from './EmptyCart';
import CartItem from './CartItem';
import axios from 'axios';

import { post } from '../../utils/paytm';
import { payUsingPaytm } from '../../service/api';

const Component = styled(Grid)(({ theme }) => ({
    padding: '30px 135px',
    display: 'flex',
    [theme.breakpoints.down('sm')]: {
        padding: '15px 0'
    }
}));

const LeftComponent = styled(Grid)(({ theme }) => ({
    paddingRight: 15,
    [theme.breakpoints.down('sm')]: {
        marginBottom: 15
    }
}));

const Header = styled(Box)`
    padding: 15px 24px;
    background: #fff;
`;

const BottomWrapper = styled(Box)`
    padding: 16px 22px;
    background: #fff;
    box-shadow: 0 -2px 10px 0 rgb(0 0 0 / 10%);
    border-top: 1px solid #f0f0f0;
`;

const StyledButton = styled(Button)`
    display: flex;
    margin-left: auto;
    background: #fb641b;
    color: #fff;
    border-radius: 2px;
    width: 250px;
    height: 51px;
`;

const Cart = () => {
    const cartDetails = useSelector(state => state.cart);
    const { cartItems } = cartDetails;
    const [totalPrice,setTotalPrice]=useState();
    const { id } = useParams();

    const dispatch = useDispatch();
    var price=0;
    useEffect(() => {
        if(cartItems && id !== cartItems.id)   
            dispatch(addToCart(id));
        cartItems.forEach(item => { // Changed from map to forEach
            price += item.price.mrp;
        });

        setTotalPrice(price); // Fix 2
    }, [dispatch, cartItems, id]);

    const removeItemFromCart = (id) => {
        dispatch(removeFromCart(id));
    }

	const buyNow = async () => {
		try {
			const orderUrl = "http://localhost:8000/orders";
			const { data } = await axios.post(orderUrl, { amount: totalPrice*100});
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
					const verifyUrl = "http://localhost:8000/verify";
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


    return (
        <>
        { cartItems.length ? 
            <Component container>
                <LeftComponent item lg={9} md={9} sm={12} xs={12}>
                    <Header>
                        <Typography style={{fontWeight: 600, fontSize: 18}}>My Cart ({cartItems?.length})</Typography>
                    </Header>
                        {   cartItems.map(item => (
                                <CartItem item={item} removeItemFromCart={removeItemFromCart}/>
                            ))
                        }
                    <BottomWrapper>
                        <StyledButton onClick={() => buyNow()} variant="contained">Place Order</StyledButton>
                    </BottomWrapper>
                </LeftComponent>
                <Grid item lg={3} md={3} sm={12} xs={12}>
                    <TotalView cartItems={cartItems} />
                </Grid>
            </Component> : <EmptyCart />
        }
        </>

    )
}

export default Cart;