import express from  'express';
import { getProductById, getProductDataById, getProducts, getProductsData } from '../controller/product-controller.js';
import { userSignUp, userLogIn } from '../controller/user-controller.js';
// import { addItemInCart } from '../controller/cart-controller.js';
import {addMoney,verifyPay } from '../controller/payment-controller.js';

const router = express.Router();

//login & signup
router.post('/signup', userSignUp);
router.post('/login', userLogIn);

router.get('/products', getProducts);
router.get('/product/:id', getProductById);
router.get('/productData', getProductsData);
router.get('/productData/:id', getProductDataById);

// router.post('/cart/add', addItemInCart);
router.post('/orders',addMoney)
router.post('/verify',verifyPay)


export default router;