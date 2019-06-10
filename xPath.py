#Po ID
<form action="json_login.json" id="login_form" data-status="step_1"/>
//*[@id="login_form"]

//div[@class="fieldset"]/../h1
#contain / text
$x('//a[contains(text(), "demobank w sam raz")]')
$x('//a[contains(@class, "logo")]')
#text
$x('//a[text()="demobank w sam raz do testów"]')
# "gwiazdka"
//*[@class="logo login"]
//a[@*="logo login"]
//*[@*="logo login"]

# zróbmy krótkie podsumowanie dotyczące wyszukiwania elementów:
#
# XPath powinien zawierać jak najmniej elementów w wyrażeniu, aby w przypadku zmian na stronie nie trzeba było naprawiać wszystkich wyrażeń XPath w testach, czyli ŹLE: /html/body/form/div/div/form/h1 i DOBRZE: //form[@id='login']/h1
# Staramy się używać atrybutu id
# Jeśli nie mamy id szukamy po atrybutach takich jak class, name czy tekście wewnątrz elementu
# Możemy wyszukać również rodzica lub rodzeństwo z unikalnym id i w ten sposób dostać się do naszego elementu np. [@id="login_form"]/h1.
# Łączymy poznane techniki aby odnaleźć upragniony element
# Powyższe zasady opisaliśmy w odniesieniu do XPatha, ale można i powinno się je stosować względem wszystkich sposobów znajdowania elementów.
#
# Upewnij się, że rozumiesz omówione metody wyszukiwania elementów:
#
# // co daje nam użycie podwójnego slash,
# div czym jest znacznik html i gdzie go użyć w XPath,
# @class jak dodawać atrybuty znaczników i sprawdzać ich wartości w XPath,
# * gdzie stosować gwiazdkę i z czym się to wiąże,
# text() jak stosować funkcję do wyszukiwania elementów z danym tekstem,
# contains() jak stosować funkcję do sprawdzania częściowej zawartości tekstu.
https://jaktestowac.pl/xpath-szybka-sciaga/