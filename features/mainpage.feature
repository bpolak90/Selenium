Feature: Otwarcie strony g³ównej

	Scenario: Sprawdzanie poprawnoœci otwarcia strony g³ównej
		When: Strona sie otworzy
		Then: Wyswietli sie logo sklepu
		And: Prawid³owy tytu³ w przegl¹darce
		And: Dostepny przycisk 'Sign in'
		And: W stopce strony wyswietla sie informacje o sklepie (nr telefonu, email)
	
	Scenario: Dzia³anie przycisku przekierujacego na strone fejsika sklepu
		When: Najade na logo fejsika myszka
		Then: Logo sie podswietli (zmieni kolor)
		And: Klikne w nie
		And: Przekieruje mnie na strone fejsbooka sklepu ktora otworzy sie w nowej karcie