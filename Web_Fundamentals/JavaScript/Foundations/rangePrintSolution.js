	function printRange(start, end, iterate){
			for (var i = start; i < end; i += iterate) {
				console.log(i)
			}
		}
		printRange(2, 10, 2);

		function printRangeBonus(start, end, iterate){
			if(!end){
				end = start;
				start = 0;
			}
			if(!iterate){
				iterate = 1;
			}
			for (var i = start; i < end; i += iterate) {
				console.log(i)
			}
		}
		printRange(4, 8)
		printRange(4)