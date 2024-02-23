import crypto from 'crypto'



import Razorpay from 'razorpay';

export const addMoney = async (req, res) => {
  try {
    const instance = new Razorpay({
      key_id: process.env.KEY_ID,
      key_secret: process.env.KEY_SECRET
    });

    const options = {
      amount: req.body.amount,
      currency: "INR",
      receipt: crypto.randomBytes(10).toString("hex")
    };

    instance.orders.create(options, (error, order) => {
      if (error) {
        console.log(error);
        return res.status(500).send({ message: "Something went wrong" });
      }
      res.status(200).json({ data: order });
    });
  } catch (error) {
    console.error(error);
    return res.status(500).send({ message: "Internal Server Error" });
  }
};

export const verifyPay=async(req,res)=>{
    try {
        console.log(`>>>>>>>>>>req.body>>>>`,req.body)
        const{razorpay_order_id,razorpay_payment_id,razorpay_signature}=req.body;
        const sign=razorpay_order_id+"|"+razorpay_payment_id;
        const expectedSign=crypto.createHmac("sha26",process.env.KEY_SECRET).update(sign.toString).digest("hex");
        if(razorpay_signature===expectedSign){
            return res.status(200).json({message:"Payment Verify Successfully"})
        }
        else{
            return res.status(200).json({message:"Invalid Signature Sent"})
        }
    } catch (error) {
        
    }
}
