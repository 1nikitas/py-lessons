CREATE TABLE IF NOT EXISTS 	Currencies(
				Symbol text unique,
				Name text unique,
				LastPrice integer,
				Change real,
				PercentChange text

)