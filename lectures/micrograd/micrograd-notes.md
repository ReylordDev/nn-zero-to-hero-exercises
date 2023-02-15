# micrograd

[The spelled-out intro to neural networks and backpropagation: building micrograd](https://youtu.be/VMj-3S1tku0)

[GitHub - karpathy/micrograd: A tiny scalar-valued autograd engine and a neural net library on top of it with PyTorch-like API](https://github.com/karpathy/micrograd)

[nn-zero-to-hero/lectures/micrograd at master · karpathy/nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero/tree/master/lectures/micrograd)

- Exercises:
  you should now be able to complete the following google collab, good luck!:

  [Google Colaboratory](https://colab.research.google.com/drive/1FPTx1RXtBfc4MaTkf7viZZD4U2F9gtKN?usp=sharing)

# Notes

- Leibniz Notation of the chain rule: $\displaystyle\frac{dz}{dx}=\frac{dz}{dy}\cdot \frac{dy}{dx}$
- chain-rule intuition:
  - If a car travels twice as fast as a bicycle
  - and a bicycle travels four times as fast as a walking man
  - then the car is $2\times4=8$ times as fast as the walking man
- a “+” node is basically a router in backprop, since its local gradient is 1.0 to every child.
- $\text{MSE}=\sum_n (y_n-y^* _n)^2$
  - where $y_n$ is the predicted value and $y^* _n$ is the ground truth value
  - Better loss function: Cross entropy loss
- Always remember to flush the gradients before every backward pass
  otherwise you will mount up the gradient values with every step, effectively giving a really large step size
