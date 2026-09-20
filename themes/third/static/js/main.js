"use strict";

document.addEventListener("DOMContentLoaded", function() {
	markExternalLinks();
	initBuzzword();
});

function markExternalLinks() {
	var main = document.getElementById("main");
	if (!main) {
		return;
	}
	var origin = window.location.origin;
	var links = main.querySelectorAll("a[href]");
	for (var i = 0; i < links.length; i++) {
		var href = links[i].getAttribute("href");
		if (!href || (href.indexOf("http://") !== 0 && href.indexOf("https://") !== 0)) {
			continue;
		}
		if (href.indexOf(origin) === 0) {
			continue;
		}
		links[i].setAttribute("target", "_blank");
		var rel = (links[i].getAttribute("rel") || "").split(/\s+/).filter(Boolean);
		["noopener", "noreferrer"].forEach(function(token) {
			if (rel.indexOf(token) === -1) {
				rel.push(token);
			}
		});
		links[i].setAttribute("rel", rel.join(" "));
	}
}

function initBuzzword() {
    // Pick a random buzzword to kick some asses
	// from https://calendar.vpogiba.info/otro/unicode.php
	var buzzwords = [
		"hydroponics",
		"IoT",
		"tech",
		"HiFi",
		"houseplants",
		"OSS",
		"&#127828;",
		"&#128021;",
		"&#127793;",
        "&#128027;",
        "&#128013;"
	];

	var container = document.getElementById("buzzword");
	if (!container) {
		return;
	}
	var word = buzzwords[Math.floor(Math.random() * buzzwords.length)];
	if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || typeof Typed === "undefined") {
		container.innerHTML = word;
		return;
	}
	// element content must be cleaned for typed.js
	container.innerHTML = "";

	new Typed("#buzzword", {
		strings: [word],
		typeSpeed: 30,
		loop: false,
		showCursor: true,
		onComplete: function() {
			var cursor = document.querySelector(".typed-cursor");
			if (cursor) {
				window.setTimeout(function(){ cursor.style.display = "none"; }, 333);
			}
		}
	});
}
