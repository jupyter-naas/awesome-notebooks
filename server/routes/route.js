import express from  'express';
import { getProductById, getProducts } from '../controller/product-controller.js';
import { userSignUp, userLogIn } from '../controller/user-controller.js';
// import { addItemInCart } from '../controller/cart-controller.js';
import { addPaymentGateway, paymentResponse,addMoney,verifyPay } from '../controller/payment-controller.js';

const router = express.Router();

//login & signup
router.post('/signup', userSignUp);
router.post('/login', userLogIn);

router.get('/products', getProducts);
router.get('/product/:id', getProductById);

// router.post('/cart/add', addItemInCart);
router.post('/orders',addMoney)
router.post('/verify',verifyPay)
router.post('/payment', addPaymentGateway);
router.post('/callback', paymentResponse);

export default router;