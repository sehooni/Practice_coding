# 02. 모듈 사용하기
    # 모듈 불러오기

import area

# import를 통해 모듈에 저장된 함수를 불러와 사용할 수 있다.
print(area.circle(2))
print(area.square(9))

# 상수 또한 마찬가지로 불러와서 사용이 가능하다.
print(area.PI)

# 03. 모듈을 가져오는 여러가지 방법들
    # 모듈을 불러오는 방법은 사실 여러가지가 있다.
        # 어쩔 때는 모듈에 있는 함수가 다 필요한 것이 아닌, 일부만 필요한 경우가 있다.

# 함수 자체를 가져오기
from area import circle, square

# 이 경우, 앞에 모듈 이름 작성 없이 함수만 작성하면 된다.
print(circle(2))
print(square(9))

# 우리가 원하는 이름으로도 불러올 수 있다.
    # 아래 코드는 area 모듈을 가져오는데 이름을 ar으로 지정한다는 뜻이다.
    # 단 이름을 명명할 때, 유사성을 지니도록 해야한다.
import area as ar
print(ar.circle(2))
print(ar.square(9))

    # 함수 또한 이름을 바꿀 수 있다.
from area import square as sq
print(sq(9))

# 마지막으로 한가지만 더 살펴보자
    # 아래와 같이 하면 모든 함수를 다 불러올 수 있다.
from area import *
print(square(3))
print(circle(9))
print(PI)
    # 그러나 이 방식은 어떤 함수를 가져왔는지 알 수 없고, 쓸데없는 함수까지도 호출할 수 있기 때문에 권장하지 않는다.