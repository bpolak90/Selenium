Feature: Otwarcie strony g��wnej

	Scenario: Sprawdzanie poprawno�ci otwarcia strony g��wnej
		When: Strona sie otworzy
		Then: Wyswietli sie logo sklepu
		And: Prawid�owy tytu� w przegl�darce
		And: Dostepny przycisk 'Sign in'
		And: W stopce strony wyswietla sie informacje o sklepie (nr telefonu, email)
	
	Scenario: Dzia�anie przycisku przekierujacego na strone fejsika sklepu
		When: Najade na logo fejsika myszka
		Then: Logo sie podswietli (zmieni kolor)
		And: Klikne w nie
		And: Przekieruje mnie na strone fejsbooka sklepu ktora otworzy sie w nowej karcie