# Overview

This is a technique outlined in [Leon.A.Gaty's paper, *A Neural Algorithm of Artistic Style*](https://arxiv.org/abs/1508.06576), which is a great read, and you should definitely check it out.

## 요약

특히 그림과 같은 순수 미술에서 사람들은 그림의 스타일과 그 내용 사이의 복잡한 상호작용(interplay)의 구성을 통해 독특한 시각적 경험을 만들어내는 스킬을 마스터했다. 
이러한 알고리듬적인 기초의 과정은 인공지능에서는 찾아보기 어려웠다. 그러나 **DNN모델**을 통해 사람의 행동과 비슷하게 얼굴 및 물체 인식의 방법을 증명했다. 
본 논문에선 이러한 방법에 대한 수학적 설명을 비롯하여 방법론적 설명을 소개한다. 


## **What is neural style transfer?**

Neural style transfer is an optimization technique used to take three images, a **content** image, a **style reference** image(such as an artwork by a famous painter),
and the **input** image you want to style -- and blend them together such that the input image is transformed to look like the content image,
but "painted" in the style of the style image.
The principle of neural style transfer is to define two distance functions, one that describes how different the content of two images are
,![](https://latex.codecogs.com/gif.latex?L_%7Bcontent%7D), and one that describes the difference between two images in terms of their style,
![](https://latex.codecogs.com/gif.latex?L_%7Bstyle%7D). Then, given three images, a desired style image, a desired content image,
and the input image (initialized with the content image), we try to transform the input image to minimize the content distance with the content image and its style
distance with the style image. 
In summary, we’ll take the base input image, a content image that we want to match, and the style image that we want to match. 
We’ll transform the base input image by minimizing the content and style distances (losses) with backpropagation, creating an image that matches the content of the content 
image and the style of the style image. 

## The process & result came from this code 
I used picture 
- [Effel Tower smogy january evening](https://commons.wikimedia.org/wiki/File:Effel_Tower_smogy_january_evening.jpg)-By Siren.Com [CC BY-SA 3.0(https://creativecommons.org/licenses/by-sa/3.0/)], from Wikimedia Commons 
- mage of Tuebingen — Photo By: Andreas Praefcke [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY 3.0 (https://creativecommons.org/licenses/by/3.0)], from Wikimedia Commons  
- Image of Pillars of Creation by NASA, ESA, and the Hubble Heritage Team, Public Domain
- [Arbre en fleur, Gustave Caillebotte,1882](https://commons.wikimedia.org/wiki/File:Arbre_en_fleur,_Gustave_Caillebotte,_1882.jpg)-By lbex73 [CC BY-SA 4.0(https://creativecommons.org/licenses/by-sa/4.0/)], from Wikimedia Commons.

### - fig. 1 process 1
![process4](https://user-images.githubusercontent.com/84653623/157852849-b09b4e0d-065b-4900-a6a2-98622ef569a5.png)

> *mage of Tuebingen — Photo By: Andreas Praefcke [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY 3.0 (https://creativecommons.org/licenses/by/3.0)], from Wikimedia Commons*

> *[Arbre en fleur, Gustave Caillebotte,1882](https://commons.wikimedia.org/wiki/File:Arbre_en_fleur,_Gustave_Caillebotte,_1882.jpg)-By lbex73 [CC BY-SA 4.0(https://creativecommons.org/licenses/by-sa/4.0/)], from Wikimedia Commons*

### - fig. 2 result 1
![result4](https://user-images.githubusercontent.com/84653623/157852961-ed808791-0a79-481e-b019-92450a47daa6.png)

> *mage of Tuebingen — Photo By: Andreas Praefcke [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY 3.0 (https://creativecommons.org/licenses/by/3.0)], from Wikimedia Commons*

> *[Arbre en fleur, Gustave Caillebotte,1882](https://commons.wikimedia.org/wiki/File:Arbre_en_fleur,_Gustave_Caillebotte,_1882.jpg)-By lbex73 [CC BY-SA 4.0(https://creativecommons.org/licenses/by-sa/4.0/)], from Wikimedia Commons*

**You can apply with new photo and picture.**

### - fig. 3 process 2(application)
![process2](https://user-images.githubusercontent.com/84653623/157853163-9f5a36ce-b4f7-454d-819b-6c420072b855.png)

> *[Effel Tower smogy january evening](https://commons.wikimedia.org/wiki/File:Effel_Tower_smogy_january_evening.jpg)-By Siren.Com [CC BY-SA 3.0(https://creativecommons.org/licenses/by-sa/3.0/)], from Wikimedia Commons*

> *Image of Pillars of Creation by NASA, ESA, and the Hubble Heritage Team, Public Domain*

### - fig. 4 result 2(application)
![result2](https://user-images.githubusercontent.com/84653623/157853221-0e147884-86b3-4da4-981f-2c5db7cd02cc.png)

> *[Effel Tower smogy january evening](https://commons.wikimedia.org/wiki/File:Effel_Tower_smogy_january_evening.jpg)-By Siren.Com [CC BY-SA 3.0(https://creativecommons.org/licenses/by-sa/3.0/)], from Wikimedia Commons*

> *Image of Pillars of Creation by NASA, ESA, and the Hubble Heritage Team, Public Domain*
