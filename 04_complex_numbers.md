## Refresher of complex numbers

- From number line to complex number plane. Number line is the old line with ± infinity "centered"at 0. But in maths most of the times it's better to think in planes (like real numbers axis [x-coord] and imaginary numbers axis [y-coord]).

- Basis of real axis is $\large 1$ and basis of imaginary axis is the imaginary operator $\large i = \sqrt{-1}$. FYI, i comes from the solution of the equation $$\Large x^2 +1 = 0$$ where $\large x$ needs to be equal to $\large i$

- Complex plane (maginary) can pack a lot of information into a single number. For example the number $$[\Large 2 \space 3i]$$ looks like a pair of numbers but in reality it's just one that has a `real number` $\large 2$ and and `imaginary number` $\large 3$. The $\large 3i$ is the `imaginary path` of the complex number. 

- The `magnitude` is the distance from the origin, like $\large -5$ has magnitude of $\large 5$ and `sign` negative. For complex numbers, you need `trigonometry` the derive  the magnitude.

- Addition and subtraction work as expected, aka so do operations on real wiht real and imaginary with imaginary

- `Multiplication` is a bit tricky, but not hard. It looks like multiplication expansion in algebra (cross product). Given $\large Z \cdot W$ where $\large Z$ and $\large W$ are complex numbers, the multiplication goes as follow, $$\Large Z \cdot W = (Z_r + iZ_i)(W_r + iW_i)$$ which exapnds to $$\Large Z \cdot W = Z_r W_r + Z_r  \space iW_i + iZ_i W_r + iZ_i \space iW_i$$ The last component with two $\large i$ cancel each others, as two square root of $\large -1$ multiplied together give $\large -1$ and those two imaginary components multiplied by each other become a real valued term! Then you can group terms like normal algebra.

- `Complex Conjugate`, is a particular operation on a complex number, often indicated with an asterisks $\large z \to\, z^*$. Flips the `sign` of the imaginary number and the real part of the complex number stays the same. One **interesting** property is that multiplying a complex number by its conjugate, gives a real number and no complex numbers, even though both are complex numbers --> `magnitude squared` of the complex number.

- `Division` it's also tricky. You can start by multuplying both numerator and denominator by the complex conjugate of the denominator. Now the denominator is a real valued number and no more a complex one. The result is a complex number

- `Geometric perspective` of complex numbers on planes. Now the complex number can be thought not only as a point but as the end point of a line starting from the origin. This line becomes the hypotenuse of a triangle, where the other two legs are the real part and the imaginary part of the complex number.  
We can compute the length of this line/hypotenus and the angle w.r.t. the real axis. This two quantities are called, respectively, `magnitude of a complex number` and `phase/argumnet of a complex argument`. 

- Magnitude/length of the line is taken as the two legs squared summed together (pytagorian theorem) $\large z^2 = z_r^{2} + z_i^{2}$ **NOT** including the $\large i$, which is the same as taking the square root of the number times it complex conjugate $\large = \sqrt{zz^*}$.  **Note** : including the $\large i$ in the square will output a negative number for the length of a line, which is not possible and its a common error.

- Phase: angle $\large \theta$ between the line and the real axis. $\Large \tan(\theta) = \frac{imag(Z)}{real(Z)} $
to get the angle $\Large \theta = \atan(\frac{imag(Z)}{real(Z)})$